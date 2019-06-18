import java.awt.*;
import javax.swing.*;

/**
 * 采用MVC结构
 * 视图层view
 * @author wankcn
 */

public class ViewFrame extends JFrame{

    //
    private int canvasWidth;
    private int canvasHeight;

    public ViewFrame(String title, int canvasWidth, int canvasHeight){

        super(title);
        //设置大小实际是画布的大小
        this.canvasWidth = canvasWidth;
        this.canvasHeight = canvasHeight;

        //实例画布相应的对象
        ViewCanvas canvas = new ViewCanvas();
        setContentPane(canvas);

        setResizable(false); //用户不能自由的改变窗口的大小
        //根据加载进来的内容进行一次布局整理 自动调整窗口的大小
        pack();    // 在setResizable(false)后进行pack()，防止在Windows下系统修改frame的尺寸
                   // 具体参见：http://coding.imooc.com/learn/questiondetail/26420.html

        //显示关闭窗口
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    /**
     * 计算屏幕宽和高，用于占满全屏的窗口
     * @param title
     */
    public ViewFrame(String title){

        this(title, 1024, 768);
    }

    // 提供相应getter接口供外部访问
    public int getCanvasWidth(){return canvasWidth;}
    public int getCanvasHeight(){return canvasHeight;}

    // TODO: 设置自己的数据
    private Object data;

    /**
     * 根据传进来的data数据进行相应的渲染
     * @param data 设置相应的数据类型
     */
    public void render(Object data){
        this.data = data;
        //会将ViewCanas清空，重新调用一遍paintComponent
        repaint(); //刷新JFrame中所有控件
    }

    /**
     * 画布内部类 继承JPanel 默认支持双缓存
     */
    private class ViewCanvas extends JPanel{

        public ViewCanvas(){
            // 双缓存
            super(true);
        }

        /**
         * swing需要重新绘制会自动传来一个Graphics g给paintComponent()进行绘制
         * @param g 类似一个上下文连接工具
         */
        @Override
        public void paintComponent(Graphics g) {
            super.paintComponent(g);
            //将Graphics对象转换成2D对象
            Graphics2D g2d = (Graphics2D)g;

            // 抗锯齿
            RenderingHints hints = new RenderingHints(
                    RenderingHints.KEY_ANTIALIASING,
                    RenderingHints.VALUE_ANTIALIAS_ON); //VALUE_ANTIALIAS_ON打开抗锯齿
            hints.put(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
            g2d.addRenderingHints(hints); //只需要在给g2d中添加抗锯齿

            // 具体绘制
            // TODO： 绘制自己的数据data
        }

        /**
         * 系统创建这个内部类的时候会自动调用Dimension来决定画布的大小
         */
        @Override
        public Dimension getPreferredSize(){
            return new Dimension(canvasWidth, canvasHeight);
        }
    }
}


