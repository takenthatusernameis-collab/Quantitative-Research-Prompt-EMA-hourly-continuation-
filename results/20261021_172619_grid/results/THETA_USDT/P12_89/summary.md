# EMA Hourly Continuation — THETA/USDT P12_89

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7547 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9110 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.0012 |
| sortino_ratio | -0.6217 |
| max_drawdown | 0.5418 |
| cagr | -0.2490 |
| net_avg_win | 69.8008 |
| net_avg_loss | -83.6116 |
| avg_hold_time_bars | 25.6155 |
| exposure | 0.5542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
