// The API isBadVersion is defined for you.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int s = 0;
        int e = n;
        int mid = s + (e-s)/2;
        while(s<=e){
            if(isBadVersion(mid)==true){
				if(isBadVersion(mid-1)==false)
				{
						return mid;
				}
            }
            if(isBadVersion(mid)==false){
                s = mid+1;
            }
            else{
                e = mid - 1;
            }
            mid = s + (e-s)/2;
        }
        
        return -1;
    }
};