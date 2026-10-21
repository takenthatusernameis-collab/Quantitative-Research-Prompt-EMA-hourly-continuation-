# EMA Hourly Continuation — NEAR/USDT P20_89

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.7959 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9632 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -1.5685 |
| sortino_ratio | -0.4769 |
| max_drawdown | 0.4812 |
| cagr | -0.1984 |
| net_avg_win | 74.8346 |
| net_avg_loss | -90.3647 |
| avg_hold_time_bars | 17.4702 |
| exposure | 0.3597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
