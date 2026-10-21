# EMA Hourly Continuation — TFUEL/USDT P8_55

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 823 |
| net_profit_factor | 0.6529 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -4.7093 |
| sortino_ratio | -1.9136 |
| max_drawdown | 0.8915 |
| cagr | -0.5854 |
| net_avg_win | 46.0707 |
| net_avg_loss | -55.9580 |
| avg_hold_time_bars | 10.8663 |
| exposure | 0.4047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
