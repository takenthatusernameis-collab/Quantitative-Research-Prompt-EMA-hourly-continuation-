# EMA Hourly Continuation — PUFFER/USDT P26_34

**Symbol:** PUFFER/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 785 |
| net_profit_factor | 0.3056 |
| net_win_rate | 0.4102 |
| gross_profit_factor | 0.6396 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -9.9116 |
| sortino_ratio | -4.3939 |
| max_drawdown | 0.9891 |
| cagr | -0.8936 |
| net_avg_win | 13.5195 |
| net_avg_loss | -30.7652 |
| avg_hold_time_bars | 2.7274 |
| exposure | 0.1212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
