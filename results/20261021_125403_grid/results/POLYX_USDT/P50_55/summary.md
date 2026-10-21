# EMA Hourly Continuation — POLYX/USDT P50_55

**Symbol:** POLYX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.5888 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9524 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.5677 |
| sortino_ratio | -0.5244 |
| max_drawdown | 0.4987 |
| cagr | -0.2150 |
| net_avg_win | 67.9341 |
| net_avg_loss | -104.4978 |
| avg_hold_time_bars | 4.8168 |
| exposure | 0.0442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
