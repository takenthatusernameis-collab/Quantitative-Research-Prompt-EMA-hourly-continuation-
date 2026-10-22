# EMA Hourly Continuation — AAVE/USDT P34_50

**Symbol:** AAVE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 944 |
| net_profit_factor | 0.3577 |
| net_win_rate | 0.4068 |
| gross_profit_factor | 0.8267 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -10.2801 |
| sortino_ratio | -4.5092 |
| max_drawdown | 0.9971 |
| cagr | -0.9008 |
| net_avg_win | 14.4588 |
| net_avg_loss | -27.7178 |
| avg_hold_time_bars | 2.4714 |
| exposure | 0.1060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
