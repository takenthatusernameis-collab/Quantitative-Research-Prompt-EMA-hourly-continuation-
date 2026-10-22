# EMA Hourly Continuation — IOTX/USDT P144_200

**Symbol:** IOTX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 223 |
| net_profit_factor | 0.7524 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.2387 |
| sortino_ratio | -0.2662 |
| max_drawdown | 0.3174 |
| cagr | -0.1148 |
| net_avg_win | 70.3160 |
| net_avg_loss | -97.7458 |
| avg_hold_time_bars | 8.1121 |
| exposure | 0.0822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
