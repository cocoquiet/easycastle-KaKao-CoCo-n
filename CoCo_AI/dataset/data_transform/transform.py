class Transform_to_txt_csv:
    def load(self, path):
        """Path에 따라 데이터를 로드하는 메소드입니다."""
        self.f = open(path)
    def read(self):
        """로드한 데이터를 읽는 메소드입니다."""
        self.data = self.f.read()
        self.f.close()
        return self.data