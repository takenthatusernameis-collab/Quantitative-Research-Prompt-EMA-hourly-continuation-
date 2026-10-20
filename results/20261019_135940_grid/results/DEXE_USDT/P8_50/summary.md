# EMA Hourly Continuation — DEXE/USDT P8_50

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 992 |
| net_profit_factor | 0.4144 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.7158 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -7.3478 |
| sortino_ratio | -3.2275 |
| max_drawdown | 0.9827 |
| cagr | -0.8008 |
| net_avg_win | 16.2456 |
| net_avg_loss | -29.7502 |
| avg_hold_time_bars | 12.5101 |
| exposure | 0.5641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
