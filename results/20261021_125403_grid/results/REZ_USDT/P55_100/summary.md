# EMA Hourly Continuation — REZ/USDT P55_100

**Symbol:** REZ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.8721 |
| net_win_rate | 0.5301 |
| gross_profit_factor | 1.1031 |
| gross_win_rate | 0.5301 |
| sharpe_ratio | -0.7178 |
| sortino_ratio | -0.1996 |
| max_drawdown | 0.3186 |
| cagr | -0.0907 |
| net_avg_win | 73.7197 |
| net_avg_loss | -95.3423 |
| avg_hold_time_bars | 8.5984 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
