# EMA Hourly Continuation — BSV/USDT P50_100

**Symbol:** BSV/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.4308 |
| net_win_rate | 0.4217 |
| gross_profit_factor | 0.8120 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -7.0461 |
| sortino_ratio | -2.5840 |
| max_drawdown | 0.9614 |
| cagr | -0.7246 |
| net_avg_win | 25.2492 |
| net_avg_loss | -42.7326 |
| avg_hold_time_bars | 6.4876 |
| exposure | 0.2014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
