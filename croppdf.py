from PyPDF2 import PdfFileWriter, PdfFileReader

with open("impresoras.pdf", "rb") as in_f:
    input = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input.getNumPages()

    for i in range(numPages):
        page = input.getPage(i)

        page.cropBox.upperLeft = (180, 840)
        page.cropBox.lowerRight = (841, 0)

        output.addPage(page)
    
    with open("out.pdf", "wb") as out_f:
        output.write(out_f)


    