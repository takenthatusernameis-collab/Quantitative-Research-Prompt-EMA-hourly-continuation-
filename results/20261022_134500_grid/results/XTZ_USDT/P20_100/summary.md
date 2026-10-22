# EMA Hourly Continuation — XTZ/USDT P20_100

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.6280 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 1.0533 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -3.7472 |
| sortino_ratio | -1.3329 |
| max_drawdown | 0.8107 |
| cagr | -0.4749 |
| net_avg_win | 42.6892 |
| net_avg_loss | -66.5094 |
| avg_hold_time_bars | 16.1388 |
| exposure | 0.4702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
