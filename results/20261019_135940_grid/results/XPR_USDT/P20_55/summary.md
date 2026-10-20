# EMA Hourly Continuation — XPR/USDT P20_55

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 873 |
| net_profit_factor | 0.3948 |
| net_win_rate | 0.4124 |
| gross_profit_factor | 0.7878 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -9.1159 |
| sortino_ratio | -3.8004 |
| max_drawdown | 0.9931 |
| cagr | -0.8593 |
| net_avg_win | 17.9865 |
| net_avg_loss | -31.9738 |
| avg_hold_time_bars | 5.7194 |
| exposure | 0.2270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
