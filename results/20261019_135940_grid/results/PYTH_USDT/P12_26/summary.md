# EMA Hourly Continuation — PYTH/USDT P12_26

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1368 |
| net_profit_factor | 0.4606 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8796 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -9.1485 |
| sortino_ratio | -4.7499 |
| max_drawdown | 0.9975 |
| cagr | -0.9062 |
| net_avg_win | 13.8923 |
| net_avg_loss | -24.4897 |
| avg_hold_time_bars | 2.7690 |
| exposure | 0.1722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
