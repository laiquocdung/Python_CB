namDl= int(input("nhap nam sinh cua ban"))
duCan=namDl%10
duChi=namDl%12
match duCan:
    case 0:
        Can="Canh"
    case 1:
        Can="Tan"
    case 2:
        Can="Nham"
    case 3:
        Can="Quy"
    case 4:
        Can="Giap"
    case 5:
        Can="At"
    case 6:
        Can="Binh"
    case 7:
        Can="Dinh"
    case 8:
        Can="Mau"
    case 9:
        Can="Ky"
match duChi:
    case 0:
        Chi="Than"
    case 1:
        Chi="Dau"
    case 2:
        Chi="Tuat"
    case 3:
        Chi="Hoi"
    case 4:
        Chi="Ti"
    case 5:
        Chi="Suu"
    case 6:
        Chi="Dan"
    case 7:
        Chi="Meo"
    case 8:
        Chi="Thin"
    case 9:
        Chi="Ty"
    case 10:
        Chi="Ngo"
    case 11:
        Chi="Mui"
NamAL=Can+Chi