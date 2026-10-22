# EMA Hourly Continuation — METIS/USDT P12_100

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7279 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -2.2824 |
| sortino_ratio | -0.6911 |
| max_drawdown | 0.5758 |
| cagr | -0.2722 |
| net_avg_win | 69.3730 |
| net_avg_loss | -83.1485 |
| avg_hold_time_bars | 28.1209 |
| exposure | 0.5816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
