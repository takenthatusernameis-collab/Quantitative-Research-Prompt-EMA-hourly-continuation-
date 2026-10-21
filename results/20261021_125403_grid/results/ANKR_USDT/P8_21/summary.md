# EMA Hourly Continuation — ANKR/USDT P8_21

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.6273 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.9331 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -4.6644 |
| sortino_ratio | -1.7893 |
| max_drawdown | 0.8754 |
| cagr | -0.5585 |
| net_avg_win | 44.0652 |
| net_avg_loss | -61.2324 |
| avg_hold_time_bars | 5.5916 |
| exposure | 0.1817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
