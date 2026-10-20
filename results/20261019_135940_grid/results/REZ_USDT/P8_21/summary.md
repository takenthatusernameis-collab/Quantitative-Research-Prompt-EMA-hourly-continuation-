# EMA Hourly Continuation — REZ/USDT P8_21

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1534 |
| net_profit_factor | 0.6159 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 1.0551 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -8.1900 |
| sortino_ratio | -4.5508 |
| max_drawdown | 0.9959 |
| cagr | -0.8913 |
| net_avg_win | 22.3332 |
| net_avg_loss | -31.6569 |
| avg_hold_time_bars | 3.4250 |
| exposure | 0.2424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
