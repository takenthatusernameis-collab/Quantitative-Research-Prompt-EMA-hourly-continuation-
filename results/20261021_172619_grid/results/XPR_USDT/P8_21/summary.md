# EMA Hourly Continuation — XPR/USDT P8_21

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6300 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8698 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -2.5078 |
| sortino_ratio | -0.6505 |
| max_drawdown | 0.5321 |
| cagr | -0.2574 |
| net_avg_win | 57.8220 |
| net_avg_loss | -81.7570 |
| avg_hold_time_bars | 10.0182 |
| exposure | 0.1498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
