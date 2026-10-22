# EMA Hourly Continuation — DOGE/USDT P34_50

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 896 |
| net_profit_factor | 0.2853 |
| net_win_rate | 0.3917 |
| gross_profit_factor | 0.7435 |
| gross_win_rate | 0.4308 |
| sharpe_ratio | -10.9793 |
| sortino_ratio | -4.7156 |
| max_drawdown | 0.9981 |
| cagr | -0.9168 |
| net_avg_win | 11.3528 |
| net_avg_loss | -25.6246 |
| avg_hold_time_bars | 2.6674 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
