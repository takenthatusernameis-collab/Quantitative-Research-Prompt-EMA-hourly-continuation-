# EMA Hourly Continuation — DOGE/USDT P89_200

**Symbol:** DOGE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -2.2761 |
| sortino_ratio | -0.5155 |
| max_drawdown | 0.4669 |
| cagr | -0.2109 |
| net_avg_win | 66.3031 |
| net_avg_loss | -87.7365 |
| avg_hold_time_bars | 15.9486 |
| exposure | 0.1834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
