# EMA Hourly Continuation — GRAM/USDT P12_21

**Symbol:** GRAM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.6303 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9461 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -2.1024 |
| sortino_ratio | -0.4501 |
| max_drawdown | 0.4301 |
| cagr | -0.1862 |
| net_avg_win | 63.7639 |
| net_avg_loss | -95.8391 |
| avg_hold_time_bars | 4.8153 |
| exposure | 0.0486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
