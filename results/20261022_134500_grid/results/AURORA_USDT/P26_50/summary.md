# EMA Hourly Continuation — AURORA/USDT P26_50

**Symbol:** AURORA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.3776 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.8321 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -9.0266 |
| sortino_ratio | -3.5917 |
| max_drawdown | 0.9901 |
| cagr | -0.8399 |
| net_avg_win | 19.2507 |
| net_avg_loss | -33.9865 |
| avg_hold_time_bars | 5.3256 |
| exposure | 0.1888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
