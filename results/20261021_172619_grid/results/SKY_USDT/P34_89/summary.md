# EMA Hourly Continuation — SKY/USDT P34_89

**Symbol:** SKY/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 0.9924 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -2.1539 |
| sortino_ratio | -0.6575 |
| max_drawdown | 0.5338 |
| cagr | -0.2605 |
| net_avg_win | 70.9622 |
| net_avg_loss | -94.4723 |
| avg_hold_time_bars | 11.6038 |
| exposure | 0.2400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
