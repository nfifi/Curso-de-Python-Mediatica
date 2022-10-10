#solução - usar tambem o pacote dateutil
import datetime
from dateutil.relativedelta import relativedelta # --> preciso instalar pacote --> pip install python-dateutil 

data_1 = datetime.datetime.strptime(input('Qual a data de nascimento (YYYY-MM-DD,HH:MM:SS):' ), '%Y-%m-%d,%H:%M:%S')
data_2 = datetime.datetime.now()

dif = abs(relativedelta(data_1, data_2)) #abs -> retorna valor absoluto e relativedelta é classe intervalo datas

print(f'Desde {data_1} passaram {dif.years} anos, {dif.months} meses, {dif.days} dias,{dif.hours} horas, {dif.minutes} minutos e {dif.seconds} segundos.')
