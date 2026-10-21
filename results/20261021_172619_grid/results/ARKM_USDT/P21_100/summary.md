# EMA Hourly Continuation — ARKM/USDT P21_100

**Symbol:** ARKM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7781 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -1.8170 |
| sortino_ratio | -0.5741 |
| max_drawdown | 0.4951 |
| cagr | -0.2332 |
| net_avg_win | 71.9934 |
| net_avg_loss | -86.3326 |
| avg_hold_time_bars | 16.4521 |
| exposure | 0.3672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
