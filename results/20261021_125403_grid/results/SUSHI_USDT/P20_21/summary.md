# EMA Hourly Continuation — SUSHI/USDT P20_21

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.5685 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8365 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -2.2656 |
| sortino_ratio | -0.4131 |
| max_drawdown | 0.3803 |
| cagr | -0.1728 |
| net_avg_win | 67.7086 |
| net_avg_loss | -99.0298 |
| avg_hold_time_bars | 3.8282 |
| exposure | 0.0282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
