# EMA Hourly Continuation — NEAR/USDT P20_21

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 105 |
| net_profit_factor | 0.9934 |
| net_win_rate | 0.5714 |
| gross_profit_factor | 1.3190 |
| gross_win_rate | 0.5714 |
| sharpe_ratio | 0.0107 |
| sortino_ratio | 0.0016 |
| max_drawdown | 0.1238 |
| cagr | -0.0014 |
| net_avg_win | 87.8276 |
| net_avg_loss | -117.8789 |
| avg_hold_time_bars | 4.9619 |
| exposure | 0.0237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
