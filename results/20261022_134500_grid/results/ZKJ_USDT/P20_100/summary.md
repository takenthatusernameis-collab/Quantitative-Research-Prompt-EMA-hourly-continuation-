# EMA Hourly Continuation — ZKJ/USDT P20_100

**Symbol:** ZKJ/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.1800 |
| net_win_rate | 0.2946 |
| gross_profit_factor | 0.4696 |
| gross_win_rate | 0.3622 |
| sharpe_ratio | -9.2165 |
| sortino_ratio | -2.6505 |
| max_drawdown | 0.9749 |
| cagr | -0.7661 |
| net_avg_win | 19.6100 |
| net_avg_loss | -45.5067 |
| avg_hold_time_bars | 46.9216 |
| exposure | 0.7891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
