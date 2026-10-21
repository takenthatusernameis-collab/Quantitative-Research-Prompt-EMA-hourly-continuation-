# EMA Hourly Continuation — CARV/USDT P26_100

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.6009 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.7568 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -3.3089 |
| sortino_ratio | -1.0028 |
| max_drawdown | 0.6239 |
| cagr | -0.3703 |
| net_avg_win | 56.9279 |
| net_avg_loss | -72.9754 |
| avg_hold_time_bars | 15.2351 |
| exposure | 0.3172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
