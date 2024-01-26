#include <stdio.h>

void print(int a[], int size);

void qs(int a[],int start,int end)
{
    int left,right,aux,pivot;

    left=start;
    right = end;
    pivot = a[(left+right)/2];

    do{
        while(a[left]<pivot && left<end)left++;
        while(pivot<a[right] && right > start)right--;
        if(left <=right)
        {
            aux= a[left];
            a[left]=a[right];
            a[right]=aux;
            left++;
            right--;

        }

    }while(left<=right);
    if(start<right){qs(a,start,right);}
    if(end>left){qs(a,left,end);}

}

void quicksort(int a[],int n)
{
    qs(a,0,n-1);
}

void quickSort(int a[], int n){
    qs(a, 0, n-1);
}

int main(){
    int array[]= {7,5,3,6,8,2,9,1,4};
    int size = sizeof(array)/sizeof(int);

    printf("Array: ");
    print(array, size);

    quickSort(array, size);
    printf("Result: ");
    print(array, size);
    return 0;
}

void print(int a[], int size){
    int i;
    for(i=0; i<size; i++){
        printf(" %d ", a[i]);
    }
    printf("\n");
}