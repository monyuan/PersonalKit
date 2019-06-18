import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

/**
 * 可视化器 充当控制层MVC
 * @author wankcn
 */

public class Visualizer {

    // TODO: 创建自己的数据
    private Object data;        // 数据
    private ViewFrame frame;    // 视图

    public Visualizer(int sceneWidth, int sceneHeight){

        // 初始化数据
        // TODO: 初始化数据

        // 初始化视图frame
        EventQueue.invokeLater(() -> {
            frame = new ViewFrame("Welcome", sceneWidth, sceneHeight);
            // TODO: 根据情况决定是否加入键盘鼠标事件监听器
            frame.addKeyListener(new MineKeyListener());
            frame.addMouseListener(new MineMouseListener());
            new Thread(() -> {
                run();//控制动画逻辑
            }).start();//创建完直接启动线程
        });
    }

    // 动画逻辑
    private void run(){

        // TODO: 编写自己的动画逻辑
    }

    // TODO: 根据情况决定是否实现键盘鼠标等交互事件监听器类
    private class MineKeyListener extends KeyAdapter{ }
    private class MineMouseListener extends MouseAdapter{ }

    //main函数
    public static void main(String[] args) {
        //MVC模式 指定窗口大小
        int sceneWidth = 800;
        int sceneHeight = 800;

        // TODO: 根据需要设置其他参数，初始化visualizer
        Visualizer visualizer = new Visualizer(sceneWidth, sceneHeight);
    }
}
