
# coding: utf-8

# In[11]:


f = open('nkjp_tab.txt', encoding='utf-8', mode='r')
fo = open('nkjp_3.txt', encoding='utf-8', mode='w')
for line in f:
    try:
        form, base, morf = line.split('\t')
        morf=morf.strip()
        try:
            t = morf.split(':')
            print(t)
            fo.write(form +'\t' + base + '\t' + t[0]+'\n')
        except:
            fo.write(form +'\t' + base + '\t' + morf+'\n')
    except:
        pass


# In[19]:


f = open('test2_wynik.txt', encoding='utf-8', mode='r')
#fo = open('test2_ile.txt', encoding='utf-8', mode='w')
licznik_z=0
licznik_nz=0
for line in f:
    print(line)
    try:
        form, base, morf, morf2 = line.split('\t')
        morf2=morf2.strip()
        print(morf,morf2)
        if (morf == morf2):
            licznik_z+=1
        else: 
            licznik_nz+=1
            #morf == morf2#.split(':')
            #print(t)
           # fo.write(form +'\t' + base + '\t' + t[0]+'\n')
        #except:
         #   fo.write(form +'\t' + base + '\t' + morf+'\n')
    except:
        pass
try: print(licznik_z/(licznik_z+licznik_nz))
except: pass
print(licznik_z+licznik_nz)

#dlugosc pliku tekstowego 1301174

