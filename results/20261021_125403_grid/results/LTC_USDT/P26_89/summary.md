# EMA Hourly Continuation — LTC/USDT P26_89

**Symbol:** LTC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.5833 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8116 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -3.6093 |
| sortino_ratio | -1.0782 |
| max_drawdown | 0.7261 |
| cagr | -0.3914 |
| net_avg_win | 50.8867 |
| net_avg_loss | -70.0820 |
| avg_hold_time_bars | 13.3864 |
| exposure | 0.2677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
