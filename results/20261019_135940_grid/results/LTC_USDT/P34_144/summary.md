# EMA Hourly Continuation — LTC/USDT P34_144

**Symbol:** LTC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.3285 |
| net_win_rate | 0.4037 |
| gross_profit_factor | 0.7067 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -6.5399 |
| sortino_ratio | -2.1442 |
| max_drawdown | 0.9358 |
| cagr | -0.6575 |
| net_avg_win | 20.7284 |
| net_avg_loss | -42.7135 |
| avg_hold_time_bars | 15.3394 |
| exposure | 0.3800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
