# EMA Hourly Continuation — BLUR/USDT P50_89

**Symbol:** BLUR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.8834 |
| net_win_rate | 0.5418 |
| gross_profit_factor | 1.1826 |
| gross_win_rate | 0.5418 |
| sharpe_ratio | -0.7791 |
| sortino_ratio | -0.2167 |
| max_drawdown | 0.3524 |
| cagr | -0.0972 |
| net_avg_win | 85.6935 |
| net_avg_loss | -114.6975 |
| avg_hold_time_bars | 7.3801 |
| exposure | 0.1239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
