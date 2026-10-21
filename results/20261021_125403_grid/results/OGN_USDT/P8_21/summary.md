# EMA Hourly Continuation — OGN/USDT P8_21

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.7423 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0914 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -3.0681 |
| sortino_ratio | -1.1716 |
| max_drawdown | 0.7490 |
| cagr | -0.4150 |
| net_avg_win | 59.1691 |
| net_avg_loss | -82.6842 |
| avg_hold_time_bars | 5.6276 |
| exposure | 0.1806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
