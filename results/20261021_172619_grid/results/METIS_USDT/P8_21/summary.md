# EMA Hourly Continuation — METIS/USDT P8_21

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.7423 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 1.0148 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -2.5558 |
| sortino_ratio | -0.9310 |
| max_drawdown | 0.6639 |
| cagr | -0.3480 |
| net_avg_win | 58.7105 |
| net_avg_loss | -79.3380 |
| avg_hold_time_bars | 5.5163 |
| exposure | 0.1617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
