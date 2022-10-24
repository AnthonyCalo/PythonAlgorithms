class Solution {
    public int maxResult(int[] nums, int k) {
        Deque<Integer> queue = new ArrayDeque<>();
        int[] dp = new int[nums.length];
        dp[nums.length-1] = nums[nums.length - 1];
        queue.add(nums.length-1);
        for(int i =nums.length-2; i>=0; i--){
            System.out.println("QUEUE 1: " + queue);
            // System.out.println("DP 1: ");
            for(int myint: dp){
                System.out.print("DP: " + myint + ", ");
            }
            
            int num = nums[i];
            int maxJump = i+k;
            while(queue.size() > 0 && queue.peekFirst() > maxJump){
                System.out.println("p2: " + queue);
                queue.removeFirst();
            }
            dp[i] = num + dp[queue.peek()];
            while( queue.size() > 0 && dp[queue.peekLast()] < dp[i]){
                System.out.println("p3: " + queue);
                
                queue.pollLast();
            }
            queue.add(i);
        }
        return dp[0];
    }
}