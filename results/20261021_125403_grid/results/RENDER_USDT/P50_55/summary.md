# EMA Hourly Continuation — RENDER/USDT P50_55

**Symbol:** RENDER/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 83 |
| net_profit_factor | 0.7243 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9725 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -0.9746 |
| sortino_ratio | -0.1372 |
| max_drawdown | 0.1581 |
| cagr | -0.0607 |
| net_avg_win | 81.1897 |
| net_avg_loss | -109.4248 |
| avg_hold_time_bars | 6.0602 |
| exposure | 0.0265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
