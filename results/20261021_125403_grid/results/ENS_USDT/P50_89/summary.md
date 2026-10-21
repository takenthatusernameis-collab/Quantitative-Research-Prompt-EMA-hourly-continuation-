# EMA Hourly Continuation — ENS/USDT P50_89

**Symbol:** ENS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7382 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0156 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.8327 |
| sortino_ratio | -0.4840 |
| max_drawdown | 0.4668 |
| cagr | -0.1991 |
| net_avg_win | 70.8932 |
| net_avg_loss | -96.6072 |
| avg_hold_time_bars | 8.2301 |
| exposure | 0.1268 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
