# EMA Hourly Continuation — DUSK/USDT P12_100

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.7306 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -2.2962 |
| sortino_ratio | -0.7385 |
| max_drawdown | 0.6028 |
| cagr | -0.2894 |
| net_avg_win | 65.8946 |
| net_avg_loss | -77.1705 |
| avg_hold_time_bars | 23.7140 |
| exposure | 0.5540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
