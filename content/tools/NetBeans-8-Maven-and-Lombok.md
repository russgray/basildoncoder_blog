Title: NetBeans 8, Maven, and Project Lombok
Date: 22/04/2016 13:24:46
Author: Russell Gray
Slug: netbeans-8-maven-lombok

On a personal project recently I wanted to try using [Project Lombok][1] to cut down on java boilerplate. I found much of the online documentation for this either incomplete or just wrong, so I'm documenting what I did to get things (mostly) working here in case it helps someone else.

Some of the common problems I ran into:

* The first recommendation in both [lombok's setup page][2] and [NetBeans' own][3] is to enable 'Enable Annotation Processing in Editor'. This option isn't available for maven projects, though.
* Working maven instructions such as [this blog][4] are for older versions of lombok, which were missing some features I wanted.
* More up-to-date blogs such as [this one][5] get close, but involve hacks like having to build your project twice each time you change a lombok-annotated class. Not ideal.

Here's what I did:

1. Add maven dependency for the latest lombok (I've marked it as having provided scope because I don't want `lombok.jar` in my uberjar):

        :::xml
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.16.8</version>
            <scope>provided</scope>
        </dependency>

2. Add the maven compiler plugin for lombok. Note that I disable adding the generated code to the maven build path; the resons for this will be clear later:

        :::xml
        <build>
            <plugins>
                <plugin>
                    <groupId>org.projectlombok</groupId>
                    <artifactId>lombok-maven-plugin</artifactId>
                    <version>1.16.8.0</version>
                    <executions>
                        <execution>
                            <phase>generate-sources</phase>
                            <goals>
                                <goal>delombok</goal>
                            </goals>
                            <configuration>
                                <sourceDirectory>src/main/java</sourceDirectory>
                                <addOutputDirectory>false</addOutputDirectory>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>

    With this in place, lombok should be invoked at compile time and generate classes into `target/generated-sources/delombok`. However, those generated classes aren't compiled, because we prevented the directory being added to the build path. Why? Because if we try to compile both `src/main/java` *and* `target/generated-sources/delombok` we get tons of compile errors due to duplicate class definitions (because every single class exists in both locations). We do actually need to build the generated classes though, because they are the ones that have all the generated accessors, builders etc that the rest of the code depends on. It's not as simple as just changing the `sourceDirectory` though - if you do that, NetBeans will honour it and only show `target/generated-sources/delombok` in the editor, which means you can't edit your original source!

3. We solve this with maven profiles. The idea is that we have one profile with `sourceDirectory` set to `src/main/java`, and tell NetBeans to use this profile when coding. Then, we have another profile with `sourceDirectory` set to `target/generated-sources/delombok`, and use that when compiling. Here's how.

    First set a property to contain the desired source location:

        :::xml
        <properties>
            <!-- set default source location -->
            <src.dir>src/main/java</src.dir>
        </properties>

    Then create a profile that switches the location:

        :::xml
        <profiles>
            <profile>
                <id>lombok-build</id>
                <properties>
                    <src.dir>${project.build.directory}/generated-sources/delombok</src.dir>
                </properties>
            </profile>
        </profiles>

    Finally, set the `sourceDirectory` based on this property:

        :::xml
        <build>
            <sourceDirectory>${src.dir}</sourceDirectory>
            <plugins>
                ...
            </plugins>
        </build>

    Now we have `src/main/java` as the default location, so NetBeans will allow you to edit your source properly. Then, specify lombok-build as the active profile for various actions (build, debug etc) under Project Properties->Actions->Activate Profiles. When you build within NetBeans, it will run delombok and then compile the generated source rather than the original source.

This works pretty well for me. It's not *quite* perfect - you have to remember to use the correct profile for builds outside NetBeans, e.g. from the command line or a CI server - but it's pretty close. I'm very much enjoying not having builders clogging up my code, or having to write endless toString methods. Lombok is fun!


[1]: https://projectlombok.org/
[2]: https://projectlombok.org/setup/netbeans.html
[3]: https://netbeans.org/kb/73/java/annotations-lombok.html
[4]: https://blogs.oracle.com/geertjan/entry/lombok_maven_and_netbeans
[5]: https://www.illucit.com/blog/2016/03/lombok-1-16-with-netbeans-8-1-maven/