# EMA Hourly Continuation — TURBO/USDT P89_100

**Symbol:** TURBO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.3573 |
| net_win_rate | 0.3891 |
| gross_profit_factor | 0.7004 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -8.5281 |
| sortino_ratio | -3.0925 |
| max_drawdown | 0.9638 |
| cagr | -0.7944 |
| net_avg_win | 25.8720 |
| net_avg_loss | -46.1234 |
| avg_hold_time_bars | 1.9812 |
| exposure | 0.0575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
