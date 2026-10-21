# EMA Hourly Continuation — MLK/USDT P55_89

**Symbol:** MLK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.3056 |
| net_win_rate | 0.2927 |
| gross_profit_factor | 0.4654 |
| gross_win_rate | 0.2997 |
| sharpe_ratio | -6.1776 |
| sortino_ratio | -1.4924 |
| max_drawdown | 0.8348 |
| cagr | -0.5062 |
| net_avg_win | 43.5636 |
| net_avg_loss | -58.9771 |
| avg_hold_time_bars | 7.4495 |
| exposure | 0.0968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
