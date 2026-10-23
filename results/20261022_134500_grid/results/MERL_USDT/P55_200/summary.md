# EMA Hourly Continuation — MERL/USDT P55_200

**Symbol:** MERL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6977 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8962 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.3814 |
| sortino_ratio | -0.6622 |
| max_drawdown | 0.5587 |
| cagr | -0.2641 |
| net_avg_win | 69.4976 |
| net_avg_loss | -86.4957 |
| avg_hold_time_bars | 20.3159 |
| exposure | 0.3547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
