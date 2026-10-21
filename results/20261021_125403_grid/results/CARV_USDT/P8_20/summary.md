# EMA Hourly Continuation — CARV/USDT P8_20

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.6841 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0084 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -3.3399 |
| sortino_ratio | -1.2471 |
| max_drawdown | 0.7152 |
| cagr | -0.4348 |
| net_avg_win | 54.8031 |
| net_avg_loss | -78.6549 |
| avg_hold_time_bars | 6.2340 |
| exposure | 0.1919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
