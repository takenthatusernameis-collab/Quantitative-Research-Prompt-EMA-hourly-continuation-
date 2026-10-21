# EMA Hourly Continuation — AMP/USDT P26_55

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.4250 |
| net_win_rate | 0.3728 |
| gross_profit_factor | 0.5993 |
| gross_win_rate | 0.3728 |
| sharpe_ratio | -6.0286 |
| sortino_ratio | -1.9287 |
| max_drawdown | 0.8974 |
| cagr | -0.5918 |
| net_avg_win | 34.9812 |
| net_avg_loss | -48.9227 |
| avg_hold_time_bars | 6.5602 |
| exposure | 0.1512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
