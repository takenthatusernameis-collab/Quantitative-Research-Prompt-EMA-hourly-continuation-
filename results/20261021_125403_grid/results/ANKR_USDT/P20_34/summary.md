# EMA Hourly Continuation — ANKR/USDT P20_34

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.4696 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.7146 |
| gross_win_rate | 0.4232 |
| sharpe_ratio | -4.9490 |
| sortino_ratio | -1.5127 |
| max_drawdown | 0.8300 |
| cagr | -0.5029 |
| net_avg_win | 37.9428 |
| net_avg_loss | -59.2951 |
| avg_hold_time_bars | 7.7478 |
| exposure | 0.1606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
