# EMA Hourly Continuation — ZRX/USDT P8_20

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 784 |
| net_profit_factor | 0.6126 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.9206 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -4.9570 |
| sortino_ratio | -1.9891 |
| max_drawdown | 0.8989 |
| cagr | -0.5984 |
| net_avg_win | 38.9433 |
| net_avg_loss | -55.3761 |
| avg_hold_time_bars | 5.3967 |
| exposure | 0.1923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
