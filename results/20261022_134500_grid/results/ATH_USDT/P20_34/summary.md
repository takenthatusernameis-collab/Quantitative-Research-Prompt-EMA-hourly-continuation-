# EMA Hourly Continuation — ATH/USDT P20_34

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1073 |
| net_profit_factor | 0.4658 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -8.8514 |
| sortino_ratio | -4.2331 |
| max_drawdown | 0.9934 |
| cagr | -0.8794 |
| net_avg_win | 18.0813 |
| net_avg_loss | -31.3002 |
| avg_hold_time_bars | 2.5182 |
| exposure | 0.1310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
