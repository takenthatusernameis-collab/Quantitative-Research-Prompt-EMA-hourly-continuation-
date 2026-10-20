# EMA Hourly Continuation — IOTX/USDT P34_144

**Symbol:** IOTX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.5973 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.8844 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -3.6528 |
| sortino_ratio | -1.1892 |
| max_drawdown | 0.7696 |
| cagr | -0.4322 |
| net_avg_win | 44.8228 |
| net_avg_loss | -66.7976 |
| avg_hold_time_bars | 16.3039 |
| exposure | 0.3950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
