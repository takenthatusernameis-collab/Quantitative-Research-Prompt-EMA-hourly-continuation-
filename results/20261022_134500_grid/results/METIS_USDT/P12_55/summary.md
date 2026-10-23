# EMA Hourly Continuation — METIS/USDT P12_55

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 986 |
| net_profit_factor | 0.5215 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.8302 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -6.4374 |
| sortino_ratio | -2.8366 |
| max_drawdown | 0.9704 |
| cagr | -0.7468 |
| net_avg_win | 24.0386 |
| net_avg_loss | -36.9930 |
| avg_hold_time_bars | 9.1136 |
| exposure | 0.4085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
