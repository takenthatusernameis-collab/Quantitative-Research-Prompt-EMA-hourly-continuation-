# EMA Hourly Continuation — DEEP/USDT P8_50

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.9685 |
| net_win_rate | 0.5350 |
| gross_profit_factor | 1.1414 |
| gross_win_rate | 0.5350 |
| sharpe_ratio | -0.1880 |
| sortino_ratio | -0.0698 |
| max_drawdown | 0.2203 |
| cagr | -0.0427 |
| net_avg_win | 91.4960 |
| net_avg_loss | -108.6785 |
| avg_hold_time_bars | 14.4272 |
| exposure | 0.4321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
