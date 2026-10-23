# EMA Hourly Continuation — ZKJ/USDT P50_100

**Symbol:** ZKJ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 839 |
| net_profit_factor | 0.1806 |
| net_win_rate | 0.3588 |
| gross_profit_factor | 0.5371 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -11.4084 |
| sortino_ratio | -4.7442 |
| max_drawdown | 0.9984 |
| cagr | -0.9220 |
| net_avg_win | 7.3092 |
| net_avg_loss | -22.6460 |
| avg_hold_time_bars | 6.9714 |
| exposure | 0.2659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
