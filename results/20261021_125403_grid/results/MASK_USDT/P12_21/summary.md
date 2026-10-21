# EMA Hourly Continuation — MASK/USDT P12_21

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.5694 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.9312 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -3.9934 |
| sortino_ratio | -1.2400 |
| max_drawdown | 0.7685 |
| cagr | -0.4379 |
| net_avg_win | 45.9714 |
| net_avg_loss | -71.0428 |
| avg_hold_time_bars | 5.9532 |
| exposure | 0.1272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
