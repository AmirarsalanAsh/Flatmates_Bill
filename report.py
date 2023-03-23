import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names their due
    amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatemate1_pay = str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))
        flatemate2_pay = str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add icon
        pdf.image('files/house.png', w=80, h=80)


        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=88, txt="Flatemetes Bill", border=0, align='C', ln=1)

        #Insert Perios label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=48, txt="Period:", border=0)
        pdf.cell(w=150, h=48, txt=bill.period, border=0, ln=1)

        #Insert name and due amount of the first flatemate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatemate1_pay, border=0, ln=1)

        #Insert name and due amount of the second flatemate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatemate2_pay, border=0, ln=1)

        # Change directory to files, generate and open the PDF
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
