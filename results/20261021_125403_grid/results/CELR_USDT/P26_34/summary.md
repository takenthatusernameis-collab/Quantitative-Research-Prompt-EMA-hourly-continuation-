# EMA Hourly Continuation — CELR/USDT P26_34

**Symbol:** CELR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6057 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9070 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.7368 |
| sortino_ratio | -0.7208 |
| max_drawdown | 0.5973 |
| cagr | -0.2810 |
| net_avg_win | 53.2248 |
| net_avg_loss | -81.8534 |
| avg_hold_time_bars | 4.7130 |
| exposure | 0.0721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
