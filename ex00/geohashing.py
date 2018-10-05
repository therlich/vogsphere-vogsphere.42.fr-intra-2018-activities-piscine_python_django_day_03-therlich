import hashlib
import sys
def geohash(date, opening_price, location_1, location_2):
    try:
        date_dow=str(date)+'-'+str(opening_price)
        hash_string=hashlib.md5(date_dow.encode('utf-8')).hexdigest()
        hash_int_1=int(hash_string[0:16],16)
        hash_int_2=int(hash_string[16:32],16)
        hash_1=float(hash_int_1)
        hash_2=float(hash_int_2)

        while int(hash_1)>0:
            hash_1/=10
        while int(hash_2)>0:
            hash_2/=10

        if int(location_1)>=0:
            lon=float(int(location_1))+hash_1
        else:
            lon=float(int(location_1))-hash_1

        if int(location_2)>=0:
            lat=float(int(location_2))+hash_2
        else:
            lat=float(int(location_2))-hash_2

        print("Your geohash target is: {}".format([lon, lat]))

    except:
        print("Review your arguments!")

if __name__ == '__main__':
    geohash(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
