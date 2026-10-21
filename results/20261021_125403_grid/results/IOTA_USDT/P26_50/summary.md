# EMA Hourly Continuation — IOTA/USDT P26_50

**Symbol:** IOTA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6643 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9286 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.7772 |
| sortino_ratio | -0.8333 |
| max_drawdown | 0.6312 |
| cagr | -0.3160 |
| net_avg_win | 57.9315 |
| net_avg_loss | -79.9696 |
| avg_hold_time_bars | 5.8497 |
| exposure | 0.1167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
