# EMA Hourly Continuation — FLOW/USDT P55_89

**Symbol:** FLOW/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.4229 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.8423 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -6.9555 |
| sortino_ratio | -2.5631 |
| max_drawdown | 0.9598 |
| cagr | -0.7175 |
| net_avg_win | 24.0487 |
| net_avg_loss | -43.4662 |
| avg_hold_time_bars | 4.0297 |
| exposure | 0.1235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
