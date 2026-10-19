# EMA Hourly Continuation — ONDO/USDT P144_200

**Symbol:** ONDO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.5221 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.9368 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -4.4919 |
| sortino_ratio | -1.3215 |
| max_drawdown | 0.8128 |
| cagr | -0.4807 |
| net_avg_win | 42.7961 |
| net_avg_loss | -72.4763 |
| avg_hold_time_bars | 3.7950 |
| exposure | 0.0757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
