# EMA Hourly Continuation — ETC/USDT P20_89

**Symbol:** ETC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.4583 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.8508 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -6.5766 |
| sortino_ratio | -2.5260 |
| max_drawdown | 0.9603 |
| cagr | -0.7167 |
| net_avg_win | 24.0464 |
| net_avg_loss | -42.4042 |
| avg_hold_time_bars | 10.4920 |
| exposure | 0.3596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
