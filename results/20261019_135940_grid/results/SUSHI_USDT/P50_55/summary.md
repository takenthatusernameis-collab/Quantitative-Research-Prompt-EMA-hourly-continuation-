# EMA Hourly Continuation — SUSHI/USDT P50_55

**Symbol:** SUSHI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 863 |
| net_profit_factor | 0.1831 |
| net_win_rate | 0.3407 |
| gross_profit_factor | 0.5408 |
| gross_win_rate | 0.3789 |
| sharpe_ratio | -13.0301 |
| sortino_ratio | -5.6289 |
| max_drawdown | 0.9995 |
| cagr | -0.9518 |
| net_avg_win | 7.6198 |
| net_avg_loss | -21.5034 |
| avg_hold_time_bars | 1.9977 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
