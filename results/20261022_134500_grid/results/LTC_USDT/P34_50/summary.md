# EMA Hourly Continuation — LTC/USDT P34_50

**Symbol:** LTC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 959 |
| net_profit_factor | 0.1944 |
| net_win_rate | 0.3848 |
| gross_profit_factor | 0.6897 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -12.3763 |
| sortino_ratio | -5.5847 |
| max_drawdown | 0.9994 |
| cagr | -0.9481 |
| net_avg_win | 6.5343 |
| net_avg_loss | -21.0258 |
| avg_hold_time_bars | 2.3535 |
| exposure | 0.1026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
