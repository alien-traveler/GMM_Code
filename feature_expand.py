import numpy as np

def transform(z):#即将5*9矩阵z转换为5*(9+n)矩阵的，这里暂时不考虑两个条带之间的约束和信息，所以仅考虑一个条带三个component之间有什么有用的交叉feature来扩充
    n_components=3
    means=z[:,n_components:2*n_components]
    covs=z[:,2*n_components:3*n_components]
    weights=z[:,0:n_components]
    weight_diff=np.zeros((z.shape[0],n_components*(n_components-1)/2))#第0维为band数量，第1维为components中取两个不重复的个数
    far_overlap=np.zeros((z.shape[0],n_components*(n_components-1)/2))
    near_overlap1=np.zeros((z.shape[0],n_components*(n_components-1)/2))
    near_overlap2=np.zeros((z.shape[0],n_components*(n_components-1)/2))
    sharpness=np.zeros((z.shape[0],n_components))

    for i in range(z.shape[0]):
        ind=0
        for j in range(n_components):
            for l in range(n_components):
                if j<l:
                    weight_diff[i,ind]=np.abs(np.log(weights[i,j]/weights[i,l]))#采用ln的绝对值让他刻画两者之间做除法的差距的程度
                    far_overlap[i,ind]=np.abs(np.log((np.sqrt(covs[i,j])+np.sqrt(covs[i,l]))*covs[i,j]*weights[i,l]/covs[i,l]/weights[i,j]/np.abs(means[i,j],-means[i,l])))
                    near_overlap1[i,ind]=np.abs(means[i,j]-means[i,l])/np.sqrt(max(covs[i,j],covs[i,l]))
                    if covs[i,j]/weights[i,l]/covs[i,j]*weights[i,j]>1:#j component has larger var
                        sharp_b=l
                        m_b=j
                    else:
                        sharp_b=j
                        m_b=j
                    near_overlap2[i,ind]=covs[i,sharp_b]/weights[i,sharp_b]/covs[i,m_b]*weights[i,m_b]    
                    ind+=1  
    for i in range(z.shape[0]):
        for j in range(n_components):
            sharpness[i,j]=covs[i,j]/weights[i,j]
    z_expand=np.hstack((z,weight_diff,far_overlap,near_overlap1,near_overlap2,sharpness))
    return z_expand