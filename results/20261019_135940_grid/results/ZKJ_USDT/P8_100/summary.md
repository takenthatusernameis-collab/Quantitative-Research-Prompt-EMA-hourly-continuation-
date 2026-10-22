# EMA Hourly Continuation — ZKJ/USDT P8_100

**Symbol:** ZKJ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 179 |
| net_profit_factor | 0.2948 |
| net_win_rate | 0.3743 |
| gross_profit_factor | 0.7023 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -4.9407 |
| sortino_ratio | -0.9492 |
| max_drawdown | 0.7316 |
| cagr | -0.3965 |
| net_avg_win | 44.8475 |
| net_avg_loss | -90.9984 |
| avg_hold_time_bars | 112.0223 |
| exposure | 0.9115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
