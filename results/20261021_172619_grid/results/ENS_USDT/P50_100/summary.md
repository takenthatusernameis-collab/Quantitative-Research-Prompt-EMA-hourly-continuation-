# EMA Hourly Continuation — ENS/USDT P50_100

**Symbol:** ENS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0102 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7580 |
| sortino_ratio | -0.4754 |
| max_drawdown | 0.4706 |
| cagr | -0.1965 |
| net_avg_win | 72.0823 |
| net_avg_loss | -95.8349 |
| avg_hold_time_bars | 9.8933 |
| exposure | 0.1601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
