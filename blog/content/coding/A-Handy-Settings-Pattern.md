Title: A Handy Settings Pattern
Date: 2015-02-20T11:44:20+00:00
Author: Russell Gray
Slug: a-handy-settings-pattern
Tags: coding, .net, patterns

.Net has a fairly nice [strongly-typed settings file][1], but unfortunately
the most common pattern of access is the big fat static accessor
`Settings.Default`. Whilst refactoring some old code recently to use
dependency injection, I found myself struggling a bit to manage settings
nicely so that this static wart worked correctly. I came up with the following
little pattern which, so far, works well for me so I thought I'd share it.

Firstly, in any project that needs runtime configuration, define an interface
that contains readonly properties for the data it needs.

    :::csharp
    namespace MyClassLibraryProject
    {
        public interface ISettings
        {
            string MyStringSetting { get; }
            bool SomeFlag { get; }
        }
    }

Then in any class that depends on the settings, make sure the constructor
accepts that interface (the DI container will inject it).

    :::csharp
    namespace MyClassLibraryProject
    {
        public class MyConfigurableClass : IMyConfigurableClass
        {
            private readonly ISettings _settings;

            public MyConfigurableClass(ISettings settings)
            {
                _settings = settings;
            }
        }
    }

Then, in whatever project builds your actual executable (e.g. a Console app,
Windows Service, or even just your unit tests) define your Settings.settings
file as normal, making sure that it contains settings names that match the
properties you defined. This will generate a `Settings` class for you with the
properties needed to implement the interface defined by your class library.

    :::csharp
    namespace MyExecutableProject.Properties {


        [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
        [global::System.CodeDom.Compiler.GeneratedCodeAttribute(
            "Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGenerator",
            "12.0.0.0")]
        internal sealed partial class Settings :
            global::System.Configuration.ApplicationSettingsBase {

            private static Settings defaultInstance = ((Settings)
                (global::System.Configuration.ApplicationSettingsBase.Synchronized(
                    new Settings())));

            public static Settings Default {
                get {
                    return defaultInstance;
                }
            }

            [global::System.Configuration.ApplicationScopedSettingAttribute()]
            [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
            [global::System.Configuration.DefaultSettingValueAttribute(
                "some string value")]
            public string MyStringSetting {
                get {
                    return ((string)(this["MyStringSetting"]));
                }
            }

            [global::System.Configuration.ApplicationScopedSettingAttribute()]
            [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
            [global::System.Configuration.DefaultSettingValueAttribute("False")]
            public bool SomeFlag {
                get {
                    return ((bool)(this["SomeFlag"]));
                }
            }
        }
    }


Importantly, this generated class is `partial`, so you can extend it. The
extension doesn't need to do anything other that declare that it implements
the settings interface.

    :::csharp
    // ReSharper disable once CheckNamespace
    namespace MyExecutableProject.Properties
    {
        internal partial class Settings : MyClassLibraryProject.ISettings
        {
        }
    }

Finally, in your composition root map the static accessor for this Settings
class to the interface. In this example I'm using [SimpleInjector][2].

    :::csharp
    var container = new Container();
    container.RegisterSingle<MyClassLibraryProject.ISettings>(Settings.Default);
    container.Register<MyClassLibraryProject.IMyConfigurableClass,
        MyClassLibraryProject.MyConfigurableClass>();

SimpleInjector will now automatically inject `Settings.Default` into every
instance of `MyConfigurableClass`, behind the `ISettings` interface. This of
course makes it trivial to mock settings in tests to check configurable
behaviour without having to muck around with a settings file.

    :::csharp
    [Test]
    public void TestSomething()
    {
        var settings = Mock.Of<ISettings>(
            s => s.MyStringSetting == "test with this value");
        var sut = new MyConfigurableClass(settings);

        Assert.IsTrue(sut.DoesTheRightThing());
    }

As a bonus, because this is all strongly-typed, automated renames work as you
expect. Rename a property on the interface and it will rename the property on
the Settings class automatically (at least, Resharper does - not sure about
vanilla Visual Studio).


[1]: http://bit.ly/1DC4tKk
[2]: https://simpleinjector.org/