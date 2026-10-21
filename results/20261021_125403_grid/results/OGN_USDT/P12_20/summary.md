# EMA Hourly Continuation — OGN/USDT P12_20

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6566 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 1.0267 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.0712 |
| sortino_ratio | -0.9206 |
| max_drawdown | 0.6680 |
| cagr | -0.3457 |
| net_avg_win | 57.6122 |
| net_avg_loss | -86.9510 |
| avg_hold_time_bars | 5.0776 |
| exposure | 0.1006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
