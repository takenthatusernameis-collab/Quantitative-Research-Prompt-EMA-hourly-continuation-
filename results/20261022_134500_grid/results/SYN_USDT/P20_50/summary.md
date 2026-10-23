# EMA Hourly Continuation — SYN/USDT P20_50

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.5199 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8266 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -6.1950 |
| sortino_ratio | -2.7117 |
| max_drawdown | 0.9638 |
| cagr | -0.7325 |
| net_avg_win | 23.6627 |
| net_avg_loss | -37.6557 |
| avg_hold_time_bars | 5.3316 |
| exposure | 0.2360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
