def wavelet_trasform(w):
	out=[]
	cA0=[0]*4
	cD0=[0]*4
	cA0=lowpass(w)
	cD0=highpass(w)
	cA1=[0]*2
	cD1=[0]*2
	cA1=lowpass(cA0)
	cD1=highpass(cA0)
	cA2=[0]*1
	cD2=[0]*1
	cA2=lowpass(cA1)
	cD2=highpass(cA1)
	out.extend(cA2)
	out.extend(cD2)
	out.extend(cD1)
	out.extend(cD0)
	return out

def inverse_wavelet_trasform(t):
	t1=t
	r=[]
	a=[]
	b=[]
	c=[]
	d=[]
	e=[]
	f=[]
	g=[]
	h=[]
	t[0]=t1[0]+t1[1]
	t[1]=t1[0]-t1[1]
	a.extend(t[:2])
	b.extend(t[2:4])
	c=[a[i]+b[i] for i in range(min(len(a),len(b)))]
	d=[a[i]-b[i] for i in range(min(len(a),len(b)))]
	t[:2]=c
	t[2:4]=d
	e.extend(t[:4])
	f.extend(t[4:])
	g=[e[i]+f[i] for i in range(min(len(e),len(f)))]
	h=[e[i]-f[i] for i in range(min(len(e),len(f)))]
	r.extend(g)
	r.extend(h)
	return r

def lowpass(w):
	cA=[0]*(int(len(w)/2))
	j=0
	for i in range(0,len(w),2):
		cA[j]=int((w[i]+w[i+1])/2)
		j=j+1
	return cA

def highpass(w):
	cD=[0]*(int(len(w)/2))
	j=0
	s=0
	for i in range(0,len(w),2):
		s=int((w[i]+w[i+1])/2)
		cD[j]=w[i]-s
		j=j+1
	return cD

w1=[71,67,24,26,36,32,14,18]
w2=[18,14,32,36,26,24,67,71]
t1=wavelet_trasform(w1)
t2=wavelet_trasform(w2)
r1=inverse_wavelet_trasform(t1)
r2=inverse_wavelet_trasform(t2)
print("input1=",w1)
print("Recover1=",r1)
print("input2=",w2)
print("Recover2=",r2)
