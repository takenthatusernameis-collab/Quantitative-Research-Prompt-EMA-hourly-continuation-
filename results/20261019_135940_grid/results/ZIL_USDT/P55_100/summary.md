# EMA Hourly Continuation — ZIL/USDT P55_100

**Symbol:** ZIL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.5314 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9892 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -5.0626 |
| sortino_ratio | -1.8180 |
| max_drawdown | 0.8891 |
| cagr | -0.5803 |
| net_avg_win | 33.2016 |
| net_avg_loss | -56.3394 |
| avg_hold_time_bars | 5.3959 |
| exposure | 0.1567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
