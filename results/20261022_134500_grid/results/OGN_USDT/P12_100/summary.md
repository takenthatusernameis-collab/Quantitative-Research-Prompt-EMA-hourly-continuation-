# EMA Hourly Continuation — OGN/USDT P12_100

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5666 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -4.6977 |
| sortino_ratio | -1.6493 |
| max_drawdown | 0.8767 |
| cagr | -0.5511 |
| net_avg_win | 39.6542 |
| net_avg_loss | -57.5157 |
| avg_hold_time_bars | 20.6767 |
| exposure | 0.5932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
