# EMA Hourly Continuation — PHA/USDT P12_20

**Symbol:** PHA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7638 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6945 |
| sortino_ratio | -0.4485 |
| max_drawdown | 0.4700 |
| cagr | -0.1861 |
| net_avg_win | 76.8072 |
| net_avg_loss | -100.5552 |
| avg_hold_time_bars | 5.1147 |
| exposure | 0.0790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
