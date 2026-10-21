# EMA Hourly Continuation — ZETA/USDT P26_50

**Symbol:** ZETA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.7206 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 0.9939 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -2.1955 |
| sortino_ratio | -0.6800 |
| max_drawdown | 0.5560 |
| cagr | -0.2659 |
| net_avg_win | 59.6926 |
| net_avg_loss | -83.1881 |
| avg_hold_time_bars | 6.5096 |
| exposure | 0.1376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
