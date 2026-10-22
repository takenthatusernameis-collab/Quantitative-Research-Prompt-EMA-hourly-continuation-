# EMA Hourly Continuation — ZBCN/USDT P8_20

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1805 |
| net_profit_factor | 0.3837 |
| net_win_rate | 0.4482 |
| gross_profit_factor | 0.7415 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -10.4400 |
| sortino_ratio | -6.2833 |
| max_drawdown | 0.9996 |
| cagr | -0.9565 |
| net_avg_win | 7.6915 |
| net_avg_loss | -16.2832 |
| avg_hold_time_bars | 2.6382 |
| exposure | 0.2203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
