from kafka import KafkaProducer
import login as pbbuf
import time
import threading
import redis
import fsp_common_pb2 as pb_common


class producer(object):

    def __init__(self):
        # self.kafkaCluster = "192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092"
        # self.pyproducer = KafkaProducer(bootstrap_servers=self.kafkaCluster)
        pass

    def ProducerInit(self, kafkaCluster):
        self.kafkaCluster = kafkaCluster
        self.pyproducer = KafkaProducer(bootstrap_servers=self.kafkaCluster)

    def ClientConnected(
            self,
            messageSequence,
            topicName,
            client_id,
            service_instance_id,
            app_id,
            client_name,
            response_topic):

        cpbuf = pbbuf.ClientConnected(
            messageSequence,
            client_id,
            service_instance_id,
            app_id,
            client_name,
            response_topic)
        self.pyproducer.send(topicName, cpbuf)

    def ClientDisconnected(
            self,
            messageSequence,
            topic_name,
            client_id,
            service_instance_id,
            response_topic):
        '''
        :param messageSequence:
        :param topicName:
        :param client_id:
        :param service_instance_id:
        :param response_topic:
        :return:
        '''
        client_disconnected_buf = pbbuf.ClientDisconnected(
            messageSequence, client_id, service_instance_id, response_topic)
        self.pyproducer.send(topic_name, client_disconnected_buf)

    def CreateStream(
            self,
            messageSequence,
            topic_name,
            app_id,
            stream_type,
            stream_property,
            response_topic):
        createstream_buf = pbbuf.CreateStream(
            messageSequence,
            app_id,
            stream_type,
            stream_property,
            response_topic)
        self.pyproducer.send(topic_name, createstream_buf)

    def RFCreateStream(
            self,
            messageSequence,
            topic_name,
            app_id,
            response_topic):

        stream_type = pb_common.StreamType.Value("EnumVideoStream")
        stream_property = pb_common.StreamProperty.Value("EnumReliable")
        createstream_buf = pbbuf.CreateStream(
            messageSequence,
            app_id,
            stream_type,
            stream_property,
            response_topic)
        self.pyproducer.send(topic_name, createstream_buf)

    def CheckStreamPublishToken(
            self,
            messageSequence,
            topic_name,
            stream_id,
            stream_public_token,
            response_topic):
        checkstreampublishtoken_buf = pbbuf.CheckStreamPublishToken(
            messageSequence, stream_id, stream_public_token, response_topic)
        self.pyproducer.send(topic_name, checkstreampublishtoken_buf)

    def PublishStream(
            self,
            messageSequence,
            topic_name,
            stream_id,
            client_id,
            client_ip,
            response_topic):
        publishstreamcp_buf = pbbuf.PublishStream(
            messageSequence, stream_id, client_id, client_ip, response_topic)
        self.pyproducer.send(topic_name, publishstreamcp_buf)

    def GetSuperiorStreamServer(
        self,
        messageSequence,
        topic_name, stream_id,
        service_instance_id,
        response_topic):
        GetSuperiorStreamServer_buf = pbbuf.GetSuperiorStreamServer(
            messageSequence, stream_id, service_instance_id, response_topic)

        self.pyproducer.send(topic_name, GetSuperiorStreamServer_buf)

    def GetStreamServers(
            self,
            messageSequence,
            topic_name,
            stream_id,
            client_id,
            client_ip,
            exception_servers,
            response_topic):
        getstreamserverscp_buf = pbbuf.GetStreamServers(
            messageSequence,
            stream_id,
            client_id,
            client_ip,
            exception_servers,
            response_topic)
        self.pyproducer.send(topic_name, getstreamserverscp_buf)

    def ChannelConnected(
            self,
            messageSequence,
            topic_name,
            client_id,
            service_instance_id,
            stream_id,
            direction,
            response_topic):
        if direction == "Sending":
            channerlconnected_buf = pbbuf.ChannelConnected(
                messageSequence,
                client_id,
                service_instance_id,
                stream_id,
                pb_common.DataDirection.Value('Sending'),
                response_topic)

        elif direction == "Receiving":
            channerlconnected_buf = pbbuf.ChannelConnected(
                messageSequence,
                client_id,
                service_instance_id,
                stream_id,
                pb_common.DataDirection.Value('Receiving'),
                response_topic)
        else:
            print "Please set the DataDirection!!"
            # producer.pyproducer.send(topic_name,channerlconnected_buf)

        if channerlconnected_buf:
            self.pyproducer.send(topic_name, channerlconnected_buf)
        else:
            print "The ChannelConnected buf is null, nothing send to the SC Cluster"

    def QueryDB_clientConnected(
            self,
            messageSequence,
            topicName,
            client_id,
            service_instance_id,
            app_id,
            client_name,
            response_topic,
            redis_host):

        self.ClientConnected(
            messageSequence,
            topicName,
            client_id,
            service_instance_id,
            app_id,
            client_name,
            response_topic)
        r = redis.StrictRedis(host=redis_host, port='6379', db=0)
        query_result = r.get('client_proxy:' + client_id)

        if service_instance_id in query_result:
            print "find cp service instance id: %s in db successfully" % service_instance_id
            return True
        else:
            print "fail to find cp service instance id: %s in db " % service_instance_id
            return False

    def ReadFile(self):
        f = open("a.txt", 'r')
        rep_str = f.readlines()
        print rep_str[0]
        rsp = rep_str[0]
        f.close()

        if "created stream" in rsp:
            stream_id = rsp.split("created stream")[1]
            stream_id = stream_id.strip(" ")
            print stream_id
            app_id = producer.r.hget(stream_id, "app_id")
            print app_id
            return app_id

    def ReadStreamIDForChannelConnected(self):
        f = open("a.txt", 'r')
        rsp_str = f.readlines()
        rsp_str = rsp_str[0]
        stream_id = rsp_str.split("stream")[1]
        stream_id = stream_id.strip(" ")
        f.close()
        return stream_id

    def CheckChannelConnected(self, clientid, streamid):
        f = open("a.txt", 'r')
        rsp_str = f.readlines()
        rsp_str = rsp_str[0]
        if clientid in rsp_str and streamid in rsp_str:
            print rsp_str
            return True
        else:
            print "Fail to find the client id and stream id in rsp msg!"
            return False


a = producer()
a.ProducerInit("192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092")
# a.ClientConnected(1,"sc_instance103","1;chenming","cp_instance160","1","aguang","cp_instance160")
a.ClientConnected(
    1,
    "sc_group624",
    "1;chenmingdddsdreooppp",
    "cp_instance160",
    "1",
    "aguang",
    "cp_instance160")
a.ClientConnected(
    1,
    "sc_group624",
    "1;chenming",
    "cp_instance160",
    "1",
    "aguang",
    "cp_instance160")
# bug http://192.168.5.68/zentao/bug-view-14863.html
# a.ClientDisconnected(1,"sc_instance103","1;chenming","cp_instance160","cp_instance160")
# a.CreateStream(1,"sc_instance103","1",pb_common.StreamType.Value("EnumVideoStream"),pb_common.StreamProperty.Value("EnumReliable"),"cp_instance160")
# bug http://192.168.5.68/zentao/bug-view-14864.html
# a.CheckStreamPublishToken(1,"sc_instance103","9a708ccd-9d14-4d9d-bb3b-663142b2ef83","wzHFFJh6qMtB8DPE4XSM","cp_instance160")
# a.PublishStream(1,"sc_instance103","e9e24baf-a1bf-4d20-b11a-38032ad79245","1;chenming","1.0.1.1","cp_instance160")
# a.GetStreamServers(1,"sc_instance103","e9e24baf-a1bf-4d20-b11a-38032ad79245","1;chenming","1.0.1.1","","cp_instance160")
# a.ChannelConnected(1,"sc_instance103","1;chenming","ss1","e9e24baf-a1bf-4d20-b11a-38032ad79245","Receiving","cp_instance160")
