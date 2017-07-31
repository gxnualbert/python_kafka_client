import hessianlib
class Rule(object):
    def __init__(self):
        pass
 
   
    def get_instance(self,url,client_ip,servicename):
        proxy = hessianlib.Hessian('http://'+url+':10086/com.fsmeeting.fsp.rpc.rule.IRuleService')
        try:
            # print proxy.chooseServiceInstance('1.0.1.1','gs')
            print proxy.chooseServiceInstance(client_ip,servicename)
        except Exception, v:

            print 'May be the rule service is not start, please start it!!!'


# a=Rule()
# a.get_instance("192.168.7.71","1.0.1.1","gs")


