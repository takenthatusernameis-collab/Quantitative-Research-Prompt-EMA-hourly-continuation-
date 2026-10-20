# EMA Hourly Continuation — LISTA/USDT P89_144

**Symbol:** LISTA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.5521 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8373 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -4.1639 |
| sortino_ratio | -1.3172 |
| max_drawdown | 0.7724 |
| cagr | -0.4656 |
| net_avg_win | 44.4700 |
| net_avg_loss | -67.8105 |
| avg_hold_time_bars | 5.7403 |
| exposure | 0.1308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
