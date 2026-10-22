# EMA Hourly Continuation — ILV/USDT P50_100

**Symbol:** ILV/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7711 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 1.0217 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.8305 |
| sortino_ratio | -0.5191 |
| max_drawdown | 0.5034 |
| cagr | -0.2123 |
| net_avg_win | 77.8783 |
| net_avg_loss | -100.4776 |
| avg_hold_time_bars | 8.8900 |
| exposure | 0.1580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
