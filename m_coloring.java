import java.io.*;
import java.util.*;

/**
 * 인접한 정점들 사이에 색이 중복되지 않도록 색칠하는 방법을 모두 출력
 * 다른 색으로 할 수 없으면 NONE 출력
 * 
 * 1: n(정점개수 10이하) c(최대 색 1~3)
 * -: 인접행렬
 * 
 * 각 정점에 몇 번째 색이 칠해졌는지 출력. -> c1 c2 c3 c4.....
 * 모든 경우의 수를 한줄씩 출력하며, 낮은 번호의 색이 먼저 오는 경우를 먼저 출력.
 */
class Main {
	ArrayList<ArrayList<Integer>> graph;
	int[] coloring;		// 각 방에 칠해진 색 저장
	int n, c;

	SortedSet<String> result;

	public static void main(String[] args) throws Exception {
		(new Main()).start();
	}
	public void start() throws Exception {
		// 입력받기
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] tokens = br.readLine().split(" ");
		n = Integer.parseInt(tokens[0]);	// 정점 개수
		c = Integer.parseInt(tokens[1]);	// 최대 색

		graph = new ArrayList<>();
		coloring = new int[n];
		for(int i=0; i<n; i++){
			graph.add(new ArrayList<>());
			tokens = br.readLine().split(" ");
			for(int j=0; j<n; j++){
				if(tokens[j].charAt(0)=='1'){
					graph.get(i).add(j);
				}
			}
			coloring[i]=-1;
		}
		
		solve(0);
	}
	/**
	 * 뻗어나가기{
	 * 	if(promising){
	 * 		if(해를 찾은 경우){
	 * 			그대로 끝내거나 해를 답리스트에 추가
	 * 		} else{
	 * 			재귀
	 * 		}
	 * 	}
	 * }
	 * @param v
	 */
	void solve(int v){
		for(int i=1; i<=c; i++){
			if(isPromising(v, i)){
				coloring[v]=i;
				if(v==n-1){
					printAnswer();
					return;
				} else{
					solve(v+1);
				}
				coloring[v]=-1;
			}
		}
	}
	boolean isPromising(int v, int color){
		ArrayList<Integer> adj = graph.get(v);
		for(Integer i: adj){
			if(color==coloring[i])
				return false;
		}
		return true;
	}
	void printAnswer(){
		for(int i: coloring){
			System.out.print(i+" ");
		}
		coloring[n-1]=-1;
		System.out.println();
	}
}
