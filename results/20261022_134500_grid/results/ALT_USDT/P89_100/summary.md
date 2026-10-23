# EMA Hourly Continuation — ALT/USDT P89_100

**Symbol:** ALT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.3507 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.8281 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -6.8274 |
| sortino_ratio | -2.2397 |
| max_drawdown | 0.9396 |
| cagr | -0.6724 |
| net_avg_win | 22.4445 |
| net_avg_loss | -47.9000 |
| avg_hold_time_bars | 3.6913 |
| exposure | 0.0886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
