# EMA Hourly Continuation — ELON/USDT P20_26

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 162 |
| net_profit_factor | 0.6622 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9698 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.6271 |
| sortino_ratio | -0.2978 |
| max_drawdown | 0.3179 |
| cagr | -0.1270 |
| net_avg_win | 70.8307 |
| net_avg_loss | -104.3553 |
| avg_hold_time_bars | 6.3827 |
| exposure | 0.0470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
