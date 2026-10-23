# EMA Hourly Continuation — ORDI/USDT P21_100

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.6478 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9258 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -3.9414 |
| sortino_ratio | -1.4743 |
| max_drawdown | 0.8304 |
| cagr | -0.4973 |
| net_avg_win | 46.0977 |
| net_avg_loss | -63.0870 |
| avg_hold_time_bars | 11.5860 |
| exposure | 0.3676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
