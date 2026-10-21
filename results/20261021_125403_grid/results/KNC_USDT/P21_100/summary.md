# EMA Hourly Continuation — KNC/USDT P21_100

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7394 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9956 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -2.6938 |
| sortino_ratio | -0.8570 |
| max_drawdown | 0.6935 |
| cagr | -0.3262 |
| net_avg_win | 74.3565 |
| net_avg_loss | -93.9103 |
| avg_hold_time_bars | 19.6157 |
| exposure | 0.4431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
