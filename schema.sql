"사용월","호선명","지하철역","04시-05시 승차인원","04시-05시 하차인원","05시-06시 승차인원","05시-06시 하차인원","06시-07시 승차인원","06시-07시 하차인원","07시-08시 승차인원","07시-08시 하차인원","08시-09시 승차인원","08시-09시 하차인원","09시-10시 승차인원","09시-10시 하차인원","10시-11시 승차인원","10시-11시 하차인원","11시-12시 승차인원","11시-12시 하차인원","12시-13시 승차인원","12시-13시 하차인원","13시-14시 승차인원","13시-14시 하차인원","14시-15시 승차인원","14시-15시 하차인원","15시-16시 승차인원","15시-16시 하차인원","16시-17시 승차인원","16시-17시 하차인원","17시-18시 승차인원","17시-18시 하차인원","18시-19시 승차인원","18시-19시 하차인원","19시-20시 승차인원","19시-20시 하차인원","20시-21시 승차인원","20시-21시 하차인원","21시-22시 승차인원","21시-22시 하차인원","22시-23시 승차인원","22시-23시 하차인원","23시-24시 승차인원","23시-24시 하차인원","00시-01시 승차인원","00시-01시 하차인원","01시-02시 승차인원","01시-02시 하차인원","02시-03시 승차인원","02시-03시 하차인원","03시-04시 승차인원","03시-04시 하차인원","작업일자"

create database test;
use test;

create table subway(
line varchar(50),
station varchar(50),
i4 int(6),
o4 int(6),
i5 int(6),
o5 int(6),
i6 int(6),
o6 int(6),
i7 int(6),
o7 int(6),
i8 int(6),
o8 int(6),
i9 int(6),
o9 int(6),
i10 int(6),
o10 int(6),
i11 int(6),
o11 int(6),
i12 int(6),
o12 int(6),
i13 int(6),
o13 int(6),
i14 int(6),
o14 int(6),
i15 int(6),
o15 int(6),
i16 int(6),
o16 int(6),
i17 int(6),
o17 int(6),
i18 int(6),
o18 int(6),
i19 int(6),
o19 int(6),
i20 int(6),
o20 int(6),
i21 int(6),
o21 int(6),
i22 int(6),
o22 int(6),
i23 int(6),
o23 int(6),
i24 int(6),
o24 int(6),
i1 int(6),
o1 int(6),
i2 int(6),
o2 int(6),
i3 int(6),
o3 int(6)
);

use test;
select * from subway;
select line, station,i8 from subway order by i8 desc; 
select station from subway where station like '%동대문%';
select distinct station from subway where station like '%동대문%';
select count(distinct station) as cnt from subway where station like '%동대문%';
select * from subway where station='동대문역사문화공원' and line='4호선';
select i8 from subway where station='동대문역사문화공원' and line='4호선';