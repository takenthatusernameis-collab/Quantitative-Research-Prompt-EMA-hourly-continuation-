# EMA Hourly Continuation — RENDER/USDT P34_100

**Symbol:** RENDER/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.6608 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9690 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -3.3270 |
| sortino_ratio | -1.2034 |
| max_drawdown | 0.7233 |
| cagr | -0.4308 |
| net_avg_win | 50.0813 |
| net_avg_loss | -72.8647 |
| avg_hold_time_bars | 9.1181 |
| exposure | 0.2690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
