import sys


BITS_CAHAR = ['1','2','3','4','5','6','7','8','9','A']

def bits_char(n):
    #print n
    return chr(ord('A') + n - 1) 

def Num2Col(n):
    rst = ''
    while n != 0:
        ch = bits_char(n % 26)         
        n /= 26 
        rst += ch
    return rst[::-1]

def col2num(col_str):
    ans = 0
    mul = 26**(len(col_str)-1)
    for ch in col_str:
        ans += (ord(ch) - ord('A') + 1) * mul 
        mul /= 16
        #print ch, ans
    return ans

def is_letters_number_style(str):
    if str[0].isdigit():
        return False
    right_num = False
    for ch in str:
        if ch.isdigit() and right_num is False:
            right_num = True
        else if not ch.isdigit and right_num is True:
            return False
    return True

def test_num_2col():
    #print Num2Col(55)
    print col2num('BC')


def main():
    #test_num_2col()
    case_num = int(sys.stdin.readline())
    #print case_num
    for line in sys.stdin:
        str = line.rstrip()
        if is_letters_number_style(str):
            pass

        if str[0] == 'R':
            c_pos = str.find('C')
            row = int(str[1:c_pos])
            col = int(str[c_pos + 1:])
            print row, col
        else:




if __name__ == '__main__':
    main()
