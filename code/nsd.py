#!/usr/bin/env python
from pathlib import Path
import os
import click
@click.command()
@click.option('--in_file', '-i')
@click.option('--out_file', '-o', default=Path(Path.cwd() / 'nsd.txt'))
@click.option('--win_len', '-w', default=255 )
def telo(in_file, out_file, win_len):
    """
    принимает на вход длинну окна, путь к файлу формата  csv и \n
    путь к файлу для записи номеров пакетов с НСД и их колличестко \n
    пример:\n
    1. --in_file '/home/ubuntu/python/output4.csv' \n
     прочитает пакеты из файла /home/ubuntu/python/output4.csv и запишет выйходные значения в файл ./nsd.txt \n
    2 --in_file '/home/ubuntu/python/output4.csv' --out_file '/home/log.txt' -w 255 \n
    прочитает пакеты из файла /home/ubuntu/python/output4.csv и запишет выйходные значения в файл /home/log.txt
    """
    
    try:
        win = [] 
        count_nsd = 0        
        with open(in_file, 'r') as file:
            while True:
                line = file.readline()
                line = line[7:16]
                if not line:
                    print('done')
                    break
                add = '0x'
                value = line.strip()
                hex_16 = add + value
                dec = int(hex_16, 16)
                win.append(dec)
                #print(type(win[0]))
                if len(win) >= win_len + 1:
                    if win[len(win) - win_len] + 1 not in win[:]:
                        count_nsd += 1
                        with open(out_file, 'a') as o_f:
                            o_f.write(hex(win[len(win) - win_len])[2:] + '\n')                    
                    
                    if len(win) == win_len * 2 + 1:
                        win.pop(0)
        with open(out_file, 'a') as o_f:
                            o_f.write(str(count_nsd) + '\n')
        print(count_nsd)        
       
       
       
       
    except TypeError:
            print('ошибка! Использую --help')
if __name__ == '__main__':
    telo()
