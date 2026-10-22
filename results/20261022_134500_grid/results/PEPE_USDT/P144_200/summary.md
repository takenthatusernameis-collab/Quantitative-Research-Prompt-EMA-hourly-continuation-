# EMA Hourly Continuation — PEPE/USDT P144_200

**Symbol:** PEPE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.5757 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9444 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -3.7888 |
| sortino_ratio | -1.0726 |
| max_drawdown | 0.7410 |
| cagr | -0.4010 |
| net_avg_win | 52.5266 |
| net_avg_loss | -81.6363 |
| avg_hold_time_bars | 4.4419 |
| exposure | 0.0800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
