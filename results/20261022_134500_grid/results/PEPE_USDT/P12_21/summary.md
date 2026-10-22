# EMA Hourly Continuation — PEPE/USDT P12_21

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1468 |
| net_profit_factor | 0.3835 |
| net_win_rate | 0.3999 |
| gross_profit_factor | 0.7491 |
| gross_win_rate | 0.4264 |
| sharpe_ratio | -13.0592 |
| sortino_ratio | -7.0844 |
| max_drawdown | 0.9999 |
| cagr | -0.9754 |
| net_avg_win | 10.5964 |
| net_avg_loss | -18.4100 |
| avg_hold_time_bars | 2.0252 |
| exposure | 0.1351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
