# EMA Hourly Continuation — CSPR/USDT P21_34

**Symbol:** CSPR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1371 |
| net_profit_factor | 0.2456 |
| net_win_rate | 0.3676 |
| gross_profit_factor | 0.7192 |
| gross_win_rate | 0.3917 |
| sharpe_ratio | -13.9404 |
| sortino_ratio | -7.3627 |
| max_drawdown | 0.9999 |
| cagr | -0.9787 |
| net_avg_win | 6.4583 |
| net_avg_loss | -15.2876 |
| avg_hold_time_bars | 2.4734 |
| exposure | 0.1541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
