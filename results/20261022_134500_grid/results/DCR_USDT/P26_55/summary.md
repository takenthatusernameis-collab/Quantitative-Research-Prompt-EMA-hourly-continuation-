# EMA Hourly Continuation — DCR/USDT P26_55

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.4266 |
| net_win_rate | 0.4237 |
| gross_profit_factor | 0.8090 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -8.3116 |
| sortino_ratio | -3.6570 |
| max_drawdown | 0.9896 |
| cagr | -0.8342 |
| net_avg_win | 17.9102 |
| net_avg_loss | -30.8651 |
| avg_hold_time_bars | 4.5876 |
| exposure | 0.2014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
