# EMA Hourly Continuation — BONK/USDT P89_200

**Symbol:** BONK/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.5855 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8834 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -3.4726 |
| sortino_ratio | -0.9366 |
| max_drawdown | 0.7013 |
| cagr | -0.3718 |
| net_avg_win | 56.5624 |
| net_avg_loss | -81.4569 |
| avg_hold_time_bars | 12.6755 |
| exposure | 0.2166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
