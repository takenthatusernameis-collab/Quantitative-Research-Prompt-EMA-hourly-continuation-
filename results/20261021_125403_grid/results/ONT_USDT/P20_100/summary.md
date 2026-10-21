# EMA Hourly Continuation — ONT/USDT P20_100

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7082 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8886 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -2.5546 |
| sortino_ratio | -0.7990 |
| max_drawdown | 0.6398 |
| cagr | -0.3081 |
| net_avg_win | 64.9907 |
| net_avg_loss | -79.7670 |
| avg_hold_time_bars | 18.6914 |
| exposure | 0.4111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
