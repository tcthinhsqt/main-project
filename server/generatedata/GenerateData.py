import pandas as pd

class GenerateData():
    def __init__(self):
        super(GenerateData, self).__init__()

    def loaiBoXuongDong(self, data):
        data_new = []
        for i in range(len(data)):
            data_new.append(data[i].replace("\n",""))
        return data_new

    def load_data(self, filename):
        with open(filename, "r") as f:
            dataMauCauHoi = f.readlines()
        return self.loaiBoXuongDong(dataMauCauHoi)

    def taoCauHoiTuTapDuLieu(self, data, noiDungChinh):
        data_question = []
        noiDungChinhFormat = noiDungChinh.lower()
        for i in range(len(data)):
            s = data[i]
            if s.index("~") == 0:
                data_question.append(s.replace("~",noiDungChinh))
            else:
                data_question.append(s.replace("~",noiDungChinhFormat))
        return data_question

    def taoDanhSachCauTraLoi(self, dataCauHoi, noiDungCauTraLoi):
        danhSachCauTraLoi = []
        for i in range(len(dataCauHoi)):
            danhSachCauTraLoi.append(noiDungCauTraLoi)
        return danhSachCauTraLoi

    def taoDanhSachCauHoiVaTraLoi(self, dataCauHoi, noiDungCauTraLoi, noiDungChinh):
        dataCauHoi        = self.loaiBoXuongDong(dataCauHoi)
        danhSachCauHoi    = self.taoCauHoiTuTapDuLieu(dataCauHoi, noiDungChinh)
        danhSachCauTraLoi = self.taoDanhSachCauTraLoi(dataCauHoi, noiDungCauTraLoi)
        return danhSachCauHoi, danhSachCauTraLoi

    def taoBoDuLieu(self, dataCauHoi, dataTraLoiVaTomTat):
        danhSachCauHoi = []
        danhSachCauTraLoi = []
        for i in range(len(dataTraLoiVaTomTat)):
            noiDungCauTraLoi = dataTraLoiVaTomTat.iloc[i,0]
            noiDungTomTat = dataTraLoiVaTomTat.iloc[i,1]
            lst_CauHoi, lst_CauTraLoi = self.taoDanhSachCauHoiVaTraLoi(dataCauHoi, noiDungCauTraLoi, noiDungTomTat)
            for j in range(len(lst_CauHoi)):
                danhSachCauHoi.append(lst_CauHoi[j])
                danhSachCauTraLoi.append(lst_CauTraLoi[j])
        df = pd.DataFrame({"Câu hỏi": danhSachCauHoi, "Câu trả lời": danhSachCauTraLoi})
        return df

    def createValidationsData(self, data):
        id            = []
        user_id       = []
        question      = []
        answer        = []
        feedback      = []
        validate_date = []
        rank          = []
        for i in data:
            id.append(i.id)
            user_id.append(i.user_id)
            question.append(i.question)
            answer.append(i.answer)
            feedback.append(i.feedback)
            validate_date.append(i.validate_date)
            rank.append(i.rank)

        df = pd.DataFrame({
                            "Id": id,
                            "User Id": user_id,
                            "Câu hỏi": question,
                            "Câu trả lời": answer,
                            "Phản hồi": feedback,
                            "Ngày đánh giá": validate_date,
                            "Xếp hạng": rank,
                          })
        return df

    def test(self):
        return "2"