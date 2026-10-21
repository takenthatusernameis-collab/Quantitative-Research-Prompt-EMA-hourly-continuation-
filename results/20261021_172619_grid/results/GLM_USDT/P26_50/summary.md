# EMA Hourly Continuation — GLM/USDT P26_50

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.5888 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -3.6650 |
| sortino_ratio | -1.2066 |
| max_drawdown | 0.7616 |
| cagr | -0.4261 |
| net_avg_win | 42.3999 |
| net_avg_loss | -66.5075 |
| avg_hold_time_bars | 6.7372 |
| exposure | 0.1620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
