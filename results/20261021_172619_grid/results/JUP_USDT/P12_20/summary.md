# EMA Hourly Continuation — JUP/USDT P12_20

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9967 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5018 |
| sortino_ratio | -0.3516 |
| max_drawdown | 0.3676 |
| cagr | -0.1491 |
| net_avg_win | 73.1272 |
| net_avg_loss | -98.1870 |
| avg_hold_time_bars | 4.4023 |
| exposure | 0.0532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
