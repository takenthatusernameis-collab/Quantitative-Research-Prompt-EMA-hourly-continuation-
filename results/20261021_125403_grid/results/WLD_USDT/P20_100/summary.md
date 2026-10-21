# EMA Hourly Continuation — WLD/USDT P20_100

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.9761 |
| net_win_rate | 0.5367 |
| gross_profit_factor | 1.1465 |
| gross_win_rate | 0.5367 |
| sharpe_ratio | -0.0950 |
| sortino_ratio | -0.0287 |
| max_drawdown | 0.2557 |
| cagr | -0.0210 |
| net_avg_win | 90.6571 |
| net_avg_loss | -107.5860 |
| avg_hold_time_bars | 20.8968 |
| exposure | 0.4141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
