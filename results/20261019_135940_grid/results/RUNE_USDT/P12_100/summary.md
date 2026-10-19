# EMA Hourly Continuation — RUNE/USDT P12_100

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.6497 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9811 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -3.0511 |
| sortino_ratio | -0.9512 |
| max_drawdown | 0.7011 |
| cagr | -0.3687 |
| net_avg_win | 52.4862 |
| net_avg_loss | -77.2781 |
| avg_hold_time_bars | 29.4667 |
| exposure | 0.6630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
