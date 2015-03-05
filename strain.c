//algorithm to find e1,e2,e12
//let's assume you are working for one grain with n triple points,
// for k grains just call this procedure k times
int n;
cin>>n;
float x[n],y[n];//to store x and y coordinate of triple points
for(int i=0;i<n;i++)
cin>>x[i]>>y[i];
// to store vectors made by joining triple points.....nC2 vectors for n points
m=(n*(n-1))/2;
float initial_vector_x[m],initial_vector_y[m];
int k=0;
for(int i=0;i<n;i++)
{
for(int j=i+1;j<n;j++)
{
initial_vector_x[k]=x[j]-x[i];
initial_vector_y[k]=y[j]-y[i];
k++;
}
}
// make an array for final triple points and store in final_vector_x[m],final_vector_y[m]
// now from matrix initial_vector_x[m],initial_vector_y[m] and final_vector_x[m],final_vector_y[m]
// choose two vector and calculate e11,e12,e21,e22 for this pair.....similarly chose (nc2)c2 pair
// of vectors

// make a struct
p=(m*(m-1)/2);
struct final{
float e11;
float e12;
float e21;
float e22;
}
final arr[p];// now each element of array contains 4 values
for(int i=0;i<m;i++)
{
for(int j=i+1;j<m;j++)
{
//solve two linear equations with two variables twice(one for e11,e12 and one for e21 e22)
//store the value of respective e11,e12,....

}
}
//calculate the average of e11,e12,e21,e22