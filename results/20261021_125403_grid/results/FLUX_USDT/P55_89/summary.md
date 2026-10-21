# EMA Hourly Continuation — FLUX/USDT P55_89

**Symbol:** FLUX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6882 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9366 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -1.9389 |
| sortino_ratio | -0.4957 |
| max_drawdown | 0.4675 |
| cagr | -0.2028 |
| net_avg_win | 61.4164 |
| net_avg_loss | -85.9362 |
| avg_hold_time_bars | 6.5723 |
| exposure | 0.0950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
