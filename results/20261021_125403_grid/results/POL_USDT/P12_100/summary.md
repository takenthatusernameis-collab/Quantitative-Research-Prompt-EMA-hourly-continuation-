# EMA Hourly Continuation — POL/USDT P12_100

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7973 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0005 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.3921 |
| sortino_ratio | -0.4070 |
| max_drawdown | 0.4431 |
| cagr | -0.1719 |
| net_avg_win | 70.6665 |
| net_avg_loss | -89.9154 |
| avg_hold_time_bars | 32.8681 |
| exposure | 0.6230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
