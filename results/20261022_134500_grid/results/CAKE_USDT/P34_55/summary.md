# EMA Hourly Continuation — CAKE/USDT P34_55

**Symbol:** CAKE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.3049 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7496 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -9.0563 |
| sortino_ratio | -3.6875 |
| max_drawdown | 0.9906 |
| cagr | -0.8438 |
| net_avg_win | 12.7070 |
| net_avg_loss | -30.3219 |
| avg_hold_time_bars | 3.5431 |
| exposure | 0.1308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
