# import baostock as bs
from Common.CEnum import AUTYPE, DATA_FIELD, KL_TYPE
from Common.CTime import CTime
from KLine.KLine_Unit import CKLine_Unit
from .CommonStockAPI import CCommonStockApi
import pickle # fixme

class StaticStockC(CCommonStockApi):
    is_connect = None
    data = []

    def __init__(self, code, k_type=KL_TYPE.K_DAY, begin_date=None, end_date=None, autype=AUTYPE.QFQ):
        super(StaticStockC, self).__init__(code, k_type, begin_date, end_date, autype)
        with open('data.bin', 'rb') as file:
            self.data = pickle.load(file)

    def get_kl_data(self):
        cols = ['time_key', 'open', 'high', 'low', 'close', 'volume']
        for elem in self.data:
            yield CKLine_Unit(elem)


    def SetBasciInfo(self):
        pass

    @classmethod
    def do_init(cls): ...
        # if not cls.is_connect:
        #     cls.is_connect = bs.login()

    @classmethod
    def do_close(cls): ...
        # if cls.is_connect:
        #     bs.logout()
        #     cls.is_connect = None

    # def __convert_type(self):
    #     _dict = {
    #         KL_TYPE.K_DAY: 'd',
    #         KL_TYPE.K_WEEK: 'w',
    #         KL_TYPE.K_MON: 'm',
    #         KL_TYPE.K_5M: '5',
    #         KL_TYPE.K_15M: '15',
    #         KL_TYPE.K_30M: '30',
    #         KL_TYPE.K_60M: '60',
    #     }
    #     return _dict[self.k_type]
    
    # def wrapBs(self, fields, flag):
    # #     bs.login()
    # #     r = self.bbs(fields,flag)
    # #     bs.logout()
    # #     return r

    # # def bbs(self, fields, flag):
    #     print('debug bs', self.code, fields, self.begin_date, self.end_date, self.__convert_type(), flag)
        
    #     rs = bs.query_history_k_data_plus(
    #         code=self.code,
    #         fields=fields,
    #         start_date=self.begin_date,
    #         end_date=self.end_date,
    #         frequency=self.__convert_type(),
    #         adjustflag=flag,
    #     )
    #     if rs.error_code != '0':
    #         raise Exception(rs.error_msg)
    #     # print('rs',type(rs),rs)
    #     while rs.error_code == '0' and rs.next():
    #         print('.', rs.get_row_data())
    #         yield CKLine_Unit(create_item_dict(rs.get_row_data(), GetColumnNameFromFieldList(fields)))
            
        
