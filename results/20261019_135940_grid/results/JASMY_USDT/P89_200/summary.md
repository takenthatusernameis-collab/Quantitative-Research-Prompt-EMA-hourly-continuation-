# EMA Hourly Continuation — JASMY/USDT P89_200

**Symbol:** JASMY/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.8217 |
| net_win_rate | 0.5567 |
| gross_profit_factor | 1.2435 |
| gross_win_rate | 0.5594 |
| sharpe_ratio | -1.0819 |
| sortino_ratio | -0.2991 |
| max_drawdown | 0.3304 |
| cagr | -0.1350 |
| net_avg_win | 66.6626 |
| net_avg_loss | -101.8959 |
| avg_hold_time_bars | 12.2850 |
| exposure | 0.2116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
