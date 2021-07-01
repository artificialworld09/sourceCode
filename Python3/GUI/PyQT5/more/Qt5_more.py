'''
self.dir_bubble_para.setWordWrap(True) #to WordWrap
self.bubble_expanded.setVisible(False) #to make invisible

##to applye html tag
self.back_arrow.setTextFormat(Qt.RichText)
self.back_arrow.setText('&#8592;')

browse=self.sender().objectName()

self.quality_combo.currentIndexChanged.connect(self.quality_current_value)

old_pic=self.image_path.text() #to get image_path_text

self.lbl.adjustSize()
'''