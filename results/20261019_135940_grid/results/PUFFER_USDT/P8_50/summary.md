# EMA Hourly Continuation — PUFFER/USDT P8_50

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 820 |
| net_profit_factor | 0.6376 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -4.4205 |
| sortino_ratio | -1.9926 |
| max_drawdown | 0.8522 |
| cagr | -0.6124 |
| net_avg_win | 37.9589 |
| net_avg_loss | -55.3306 |
| avg_hold_time_bars | 10.0451 |
| exposure | 0.4661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
