#chuyển KB từ dạng chuỗi thành dạng dict
def KB_dict(KB):
    """transform KB from str to dict

    Parameters:
    KB (list of  str)


    Returns:
    list of dict


    """
    for i in range(len(KB)):

        #chuyển từng statement
        KB[i]=str_dict(KB[i])

    return KB

def str_dict(statement):
    """transform statetment from str to dict

    Parameters:
    statement (str)


    Returns:
    dict


    """
    #khởi tạo dict rỗng và tách token str
    res={}
    statement=statement.split(' ')

    for i in statement:

        #loại phần tử kí tự ko là OR
        if i.find('OR')==-1:

            #khởi tạo giá trị k cho phần tử trong dict
            k=1 

            #kiểm tra phủ định
            if i.find('-')!=-1:

                #lấy nhãn tên sau dấu phủ định 
                i=i[1:] 
                k=-1
            res.update({i:k})
            
    return res

def not_statement(alpha):
    """add negative sign to the statement

    Parameters:
    alpha (str)


    Returns:
    str


    """
    #thêm kí hiệu phủ định
    if alpha.find('-')==-1: 
        alpha='-'+alpha

    #loại kí hiệu phủ định
    else:
        alpha=alpha[1:] 

    return alpha


def dict_str(statement):
    """transform statement form dict to str

    Parameters:
    statement (dict)


    Returns:
    str


    """
    # khởi tạo list rỗng
    res=[] 

    #lấy values, keys của statement
    values,keys=values_keys(statement) 
    for i in range(len(keys)):

        #str tạm thời
        temp='' 

        #thêm dấu trừ nếu phủ định
        if values[i]==-1: 
            temp+='-'

        #tạo kí tự
        temp+=str(keys[i]) 
        res.append(temp)
        res.append('OR')

    #xóa phần OR cuối list 
    if len(res)>0: 
        res.pop()

    #thêm phần tử rỗng nếu statement rỗng
    else:
       res.append('{}')

    #tạo str 
    res=' '.join(res) 

    return res


def KB_str(KB):
    """transform KB from str to dict

    Parameters:
    KB (list of dict)


    Returns:
    list of str


    """
    for i in range(len(KB)):

        #chuyển từng statement
        KB[i]=dict_str(KB[i]) 

    return KB
    
def resolution(statement1, statement2):
    """resolution 2 statements

    Parameters:
    statement1 (dict),
    statement2 (dict)


    Returns:
    dict


    """
    #khởi tạo statement result
    res={} 

    #gán statement1 cho res
    res.update(statement1)

    #đếm số lần loại phần tử nghịch nhau 
    count=0 

    #đếm số phần tử trùng
    duplicate=0

    #chạy key trong statement2
    for i in list(statement2.keys()):

        # lấy giá trị của 2 statements
        value_stm1=res.get(i,0)
        value_stm2=statement2.get(i)

        #kiểm tra phần tử statement2 có tồn tại trong statement1 không

        #không tồn tại thì thêm vào
        if value_stm1==0:
            res.update({i:value_stm2}) 

        #nghịch nhau thì loại ra khỏi hàm res, tăng biến đếm count
        elif value_stm1+value_stm2==0:
            count +=1
            res.pop(i)
        
        #nếu tồn tại trùng thì tăng biến đếm duplicate
        else:
            duplicate+=1
    
    #nếu res rỗng
    if len(res)==0 and count<=1:
        return None

    #res ko hợp giải được (count = 0) hoặc hợp giải sai (count>1) hoặc có nhiều phần tử trùng (duplicate > 0)   
    if (len(res)>=max(len(statement1),len(statement2)) and count==0) or count>1 or duplicate>0:
        return []

    return res


def values_keys(statement):
    """
    Parameters:
    statement (dict)


    Returns:
    list of values,
    list of keys


    """
    return list(statement.values()),list(statement.keys())


def equal(statement1,statement2):
    """check if two statements are equal

    Parameters:
    statement1 (dict),
    statement2 (dict)


    Returns:
    true: equal,
    false: not equal


    """
    #kiểm tra độ dài
    if len(statement1)!= len(statement2):
        return False

    #kiểm tra có các phần tử giống nhau
    else:

        #duyệt các phần tử trong statement1
        values_stm1, keys_stm1=values_keys(statement1)
        for i in range(len(statement1)):

            #nếu 2 giá trị cùng key của 2 statement khác nhau return false
            if values_stm1[i]!=statement2.get(keys_stm1[i],0) :
                return False

    return True


def in_kb(statement,KB):
    """check if statement exists in KB

    Parameters:
    statement (dict),
    KB (list of dict)


    Returns:
    true: exist,
    false: not exist


    """
    #duyệt các statements trong KB
    for i in KB:

        #kiểm tra bằng nhau
        if equal(statement,i)==True:
            return True

    return False


def modify(new_statement,KB):
    """remove statements of new_statement that exist in KB

    Parameters:
    new_statement (list of dict),
    KB (list of dict)


    Returns:
    list of dict


    """
    temp=[]
    for i in new_statement:

        #kiểm tra phần tử không tồn tại trong temp và KB
        if in_kb(i,KB)==False and in_kb(i,temp)==False:
            temp.append(i)

    new_statement=temp
    return temp
            
def print_resolution_result(KB):
    """ print statements in a KB

    Parameters:
    KB (list of dict)

    """
    print(len(KB))
    KB=KB_str(KB)
    for i in KB:
        print(i)

def pl_resolution(KB,alpha):
    """resolution KB and alpha

    Parameters:
    KB (list of dict),
    alpha (str)


    Returns:
    true: correct,
    false: incorrect


    """
    #thêm phủ định alpha vào KB
    KB.append(not_statement(alpha))

    #chuyển KB về dạng list of dict
    KB=KB_dict(KB)
    k=len(KB)

    #khởi tạo KB_temp
    KB_temp=KB[:]
    
    #khởi tạo new_statement
    new_statement=[]

    #cờ dừng
    return_flag=0

    while(return_flag==0):

        #reset giá trị new_statement
        new_statement=[]

        #duyệt k phần tử đầu tiên trong KB
        for i in range(k):

            #xét tín hiệu dừng
            if return_flag==1:
                break
            
            #duyệt từng phần tử trong KB_temp
            for j in KB_temp:

                #hợp giải 
                res=resolution(KB[i],j)

                #kiểm tra hợp giải ra rỗng
                if res==None:
                    return_flag=1
                    new_statement.append({})
                    break

                #hợp giải thành công thêm vào new_statement
                if len(res)!=0:
                    new_statement.append(res)

        #lược bỏ phần tử trùng trong new_statement
        new_statement=modify(new_statement,KB)

        #cập nhật lại k phần tử đầu tiên trong KB, cập nhật KB, cập nhật KB_temp
        k=len(KB)
        KB+=new_statement
        KB_temp=new_statement[:]   

        #xuất kết quả hợp giải
        print_resolution_result(new_statement)

        #hợp giải không ra mệnh đề mới
        if len(new_statement)==0:
            return False      

    return True


if __name__ == "__main__":
    alpha='-A'
    kb=['-A OR B','-C OR B','A OR -B OR C','-B']
    res=pl_resolution(kb,alpha)
    if res==True:
        print('YES')
    else:
        print('NO')