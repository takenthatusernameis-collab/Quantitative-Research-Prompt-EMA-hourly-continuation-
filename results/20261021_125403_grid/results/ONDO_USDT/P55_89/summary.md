# EMA Hourly Continuation — ONDO/USDT P55_89

**Symbol:** ONDO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.6115 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.7878 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -2.6537 |
| sortino_ratio | -0.6045 |
| max_drawdown | 0.5228 |
| cagr | -0.2428 |
| net_avg_win | 71.2921 |
| net_avg_loss | -88.0274 |
| avg_hold_time_bars | 7.0775 |
| exposure | 0.0830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
