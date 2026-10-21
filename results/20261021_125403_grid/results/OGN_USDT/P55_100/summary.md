# EMA Hourly Continuation — OGN/USDT P55_100

**Symbol:** OGN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.5391 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.7636 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -3.8275 |
| sortino_ratio | -1.1093 |
| max_drawdown | 0.7328 |
| cagr | -0.4011 |
| net_avg_win | 46.1187 |
| net_avg_loss | -67.8535 |
| avg_hold_time_bars | 8.2212 |
| exposure | 0.1548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
