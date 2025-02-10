class Solution {

public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if (sr < 0 || sr >= image.size()){
        return image;
         } 
       if (sc < 0 || sc >= image[0].size()){
        return image;
        } 
        int pixel_c = image[sr][sc];
        image[sr][sc] = color;
        int pixel_top = sr-1 >= 0? image[sr-1][sc] : -1;
        if (pixel_top == pixel_c && pixel_top != color){
            image = floodFill(image, sr-1, sc, color);
        }
        int pixel_bot = sr+1 < image.size()? image[sr+1][sc] : -1;
        if (pixel_bot == pixel_c && pixel_bot != color){
            image = floodFill(image, sr+1, sc, color);
        }
        int pixel_right = sc+1 < image[0].size()? image[sr][sc+1] : -1;
        if (pixel_right == pixel_c && pixel_right != color){
            image = floodFill(image, sr, sc+1, color);
        }
        int pixel_left = sc-1 >= 0 ? image[sr][sc-1]: -1;
        if (pixel_left == pixel_c && pixel_left != color){
            image = floodFill(image, sr, sc-1, color);
        }
        return image;
    }

};