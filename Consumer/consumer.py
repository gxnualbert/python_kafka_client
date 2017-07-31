from kafka import KafkaConsumer
import time,struct
import fsp_sc_pb2 as pb_sc
import fsp_common_pb2 as pb_common
import sys

class consumer(object):

    def __init__(self):
        pass
    def ConsumerInit(self,kafkaCluster):
        self.kafkaCluster = kafkaCluster

    def ResopnseParse(self,RspObj):
        CommonResponse_obj = pb_common.CommonResponse()
        CommonResponse_obj = RspObj.response
        print CommonResponse_obj.response_code
        print CommonResponse_obj.response_msg
        return CommonResponse_obj
    def WriteTxtFile(self,CommonResponse_obj):
        f = open("a.txt", 'w')
        f.write(CommonResponse_obj.response_msg)
        f.close()

    def ClientConnectedRsp(self,consumer_topic,msg_topic):
        '''
        This function is using for consume data which produce by SC
        After SC finished consume the data which produce by CP, SC will produce data as CP's respone

        :param consume_topic: this topic used for this program to comsume data
        :param msg_topic: this topic used for unserialsize message in 'fmt'
        :param kafkaCluster:
        :return:
        '''
        consumer = KafkaConsumer(consumer_topic,bootstrap_servers=self.kafkaCluster)

        for msg in consumer:
            ClientConnectedbuf=msg.value

            fmt = "!BBqB%dsi%ds" % (len(msg_topic), (len(ClientConnectedbuf) - 15 - len(msg_topic)))
            unseriasize_msg = struct.unpack(fmt, ClientConnectedbuf)

            ClientConnectedRsp_obj = pb_sc.ClientConnectedRsp()
            ClientConnectedRsp_obj.ParseFromString(unseriasize_msg[6])

            CommonResponse_obj=self.ResopnseParse(ClientConnectedRsp_obj)

            self.WriteTxtFile(CommonResponse_obj)


    def ClientDisConnectedRep(self,consumer_topic,msg_topic):

        consumer = KafkaConsumer(consumer_topic,bootstrap_servers=self.kafkaCluster)

        for msg in consumer:
            ClientDisConnectedbuf=msg.value

            fmt = "!BBqB%dsi%ds" % (len(msg_topic), (len(ClientDisConnectedbuf) - 15 - len(msg_topic)))
            unseriasize_msg = struct.unpack(fmt, ClientDisConnectedbuf)

            ClientDisConnectRep_obj=pb_sc.ClientDisconnectedRsp()
            ClientDisConnectRep_obj.ParseFromString(unseriasize_msg[6])

            CommonResponse_obj = self.ResopnseParse(ClientDisConnectRep_obj)

            self.WriteTxtFile(CommonResponse_obj)

    def CreateStreamRsp(self,consume_topic,msg_topic):

        consumer = KafkaConsumer(consume_topic,bootstrap_servers=self.kafkaCluster)

        for msg in consumer:

            createstreamrsp_buf=msg.value

            fmt="!BBqB%dsi%ds" % (len(msg_topic), (len(createstreamrsp_buf) - 15 - len(msg_topic)))
            unseriasize_msg=struct.unpack(fmt,createstreamrsp_buf)

            CreateStreamRsp_Obj=pb_sc.CreateStreamRsp()
            CreateStreamRsp_Obj.ParseFromString(unseriasize_msg[6])

            CommonResponse_obj = self.ResopnseParse(CreateStreamRsp_Obj)
            print CommonResponse_obj
            self.WriteTxtFile(CommonResponse_obj)


    def CheckStreamPublishTokenRsp(self,consume_topic,msg_topic):

        consumer = KafkaConsumer(consume_topic,bootstrap_servers=self.kafkaCluster)

        for msg in consumer:

            checkstreampublishtokenrsp_buf=msg.value

            fmt="!BBqB%dsi%ds" % (len(msg_topic), (len(checkstreampublishtokenrsp_buf) - 15 - len(msg_topic)))
            unseriasize_msg=struct.unpack(fmt,checkstreampublishtokenrsp_buf)

            CheckStreamPublishTokenRsp_Obj=pb_sc.CheckStreamPublishTokenRsp()

            CheckStreamPublishTokenRsp_Obj.ParseFromString(unseriasize_msg[6])

            CommonResponse_obj = self.ResopnseParse(CheckStreamPublishTokenRsp_Obj)

            self.WriteTxtFile(CommonResponse_obj)

    def PublishStreamRsp(self,consume_topic,msg_topic):

        consumer = KafkaConsumer(consume_topic,bootstrap_servers=self.kafkaCluster)

        for msg in consumer:

            publishstreamrsp_buf=msg.value

            fmt="!BBqB%dsi%ds" % (len(msg_topic), (len(publishstreamrsp_buf) - 15 - len(msg_topic)))
            unseriasize_msg=struct.unpack(fmt,publishstreamrsp_buf)

            PublishStreamRsp_obj=pb_sc.PublishStreamRsp()
            PublishStreamRsp_obj.ParseFromString(unseriasize_msg[6])

            CommonResponse_obj = self.ResopnseParse(PublishStreamRsp_obj)

            self.WriteTxtFile(CommonResponse_obj)

    def GetStreamServersRsp(self,consume_topic,msg_topic):

        consumer = KafkaConsumer(consume_topic, bootstrap_servers=self.kafkaCluster)

        for msg in consumer:

            getstreamserversrsp_buf=msg.value

            fmt = "!BBqB%dsi%ds" % (len(msg_topic), (len(getstreamserversrsp_buf) - 15 - len(msg_topic)))
            unseriasize_msg = struct.unpack(fmt, getstreamserversrsp_buf)

            GetStreamServersRsp_Obj = pb_sc.GetStreamServersCPRsp()
            GetStreamServersRsp_Obj.ParseFromString(unseriasize_msg[6])

            CommonResponse_obj = self.ResopnseParse(GetStreamServersRsp_Obj)

            self.WriteTxtFile(CommonResponse_obj)


    def ChannelConnectedRsp(self,consume_topic,msg_topic):

        consumer = KafkaConsumer(consume_topic, bootstrap_servers=self.kafkaCluster)

        for msg in consumer:

            channelconnectedrsp_buf=msg.value

            fmt = "!BBqB%dsi%ds" % (len(msg_topic), (len(channelconnectedrsp_buf) - 15 - len(msg_topic)))
            unseriasize_msg = struct.unpack(fmt, channelconnectedrsp_buf)

            ChannelConnectedRsp_Obj = pb_sc.ChannelConnectedRsp()
            ChannelConnectedRsp_Obj.ParseFromString(unseriasize_msg[6])

            CommonResponse_obj = self.ResopnseParse(ChannelConnectedRsp_Obj)

            self.WriteTxtFile(CommonResponse_obj)


# consumeSC("cp_test1","sc_test_instance174")

# consue()

#here  sprint kk                                    c_test_instance103 is the topic that producer used to send message
# ClientConnectedRsp("cp_test1","sc_instance103","192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092")
# ClientDisConnectRep("cp_test1","sc_test_instance174","192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092")
# ClientDisConnectRep("cp_test1","sc_test_instance174","192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092")
# CreateStreamSPRsp("cp_test1","sc_test_instance174","192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092")
# CheckStreamPublishTokenRsp("cp_test1","sc_test_instance174","192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092")

# PublishStreamCPRsp("cp_test1","sc_test_instance174","192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092")
# GetStreamServersCPRsp("cp_test1","sc_test_instance174","192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092")
# ChannelConnectedRsp("cp_test1","sc_test_instance174","192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092")

b=consumer()
kafka_cluster="192.168.7.63:9092,192.168.7.64:9092,192.168.7.65:9092"
b.ConsumerInit(kafka_cluster)
b.ClientConnectedRsp("cp_instance160","sc_instance103")
# b.ClientDisConnectedRep("cp_instance160","sc_instance103")
b.CreateStreamRsp("cp_instance160","sc_instance103")
# b.CheckStreamPublishTokenRsp("cp_instance160","sc_instance103")
# b.ChannelConnectedRsp("cp_instance160","sc_instance103")
