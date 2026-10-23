# EMA Hourly Continuation — CELR/USDT P89_200

**Symbol:** CELR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.5925 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8843 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -3.2189 |
| sortino_ratio | -0.9052 |
| max_drawdown | 0.6701 |
| cagr | -0.3488 |
| net_avg_win | 52.2451 |
| net_avg_loss | -75.8105 |
| avg_hold_time_bars | 12.0427 |
| exposure | 0.2169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
