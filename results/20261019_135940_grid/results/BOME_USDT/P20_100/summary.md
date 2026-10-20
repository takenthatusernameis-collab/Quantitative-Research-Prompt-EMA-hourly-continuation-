# EMA Hourly Continuation — BOME/USDT P20_100

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.5761 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.7918 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -3.8033 |
| sortino_ratio | -1.3045 |
| max_drawdown | 0.8093 |
| cagr | -0.4638 |
| net_avg_win | 39.6729 |
| net_avg_loss | -57.4186 |
| avg_hold_time_bars | 16.9077 |
| exposure | 0.4580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
