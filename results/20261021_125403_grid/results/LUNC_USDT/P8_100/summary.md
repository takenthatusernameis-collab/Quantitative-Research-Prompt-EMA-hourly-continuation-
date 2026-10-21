# EMA Hourly Continuation — LUNC/USDT P8_100

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.6726 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8505 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -2.7561 |
| sortino_ratio | -0.8983 |
| max_drawdown | 0.6584 |
| cagr | -0.3387 |
| net_avg_win | 54.3913 |
| net_avg_loss | -69.9699 |
| avg_hold_time_bars | 25.9791 |
| exposure | 0.6211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
