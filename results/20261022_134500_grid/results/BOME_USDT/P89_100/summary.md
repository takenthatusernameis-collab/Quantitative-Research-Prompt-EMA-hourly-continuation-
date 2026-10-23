# EMA Hourly Continuation — BOME/USDT P89_100

**Symbol:** BOME/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.3009 |
| net_win_rate | 0.3981 |
| gross_profit_factor | 0.6294 |
| gross_win_rate | 0.4265 |
| sharpe_ratio | -8.3992 |
| sortino_ratio | -3.0312 |
| max_drawdown | 0.9804 |
| cagr | -0.7875 |
| net_avg_win | 16.7323 |
| net_avg_loss | -36.7767 |
| avg_hold_time_bars | 2.0284 |
| exposure | 0.0584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
