# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 
# 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

def test() :
    x = int(input())
    y = int(input())

    if y<2 : 
        print(-1)
        return
    is_prime = [True] * (y+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2,int(y**0.5)+1) :
        if is_prime[i] :
            for j in range(i*i,y+1,i):
                is_prime[j] = False
    primes = [i for i in range(y+1) if is_prime[i]]
    answer = list(filter(lambda n : n>=x,primes))
    if(len(answer)==0):
        print(-1)
        return
    print(sum(answer))
    print(answer[0])


test()