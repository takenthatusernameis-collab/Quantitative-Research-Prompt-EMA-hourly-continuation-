# EMA Hourly Continuation — FLOW/USDT P89_200

**Symbol:** FLOW/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.5717 |
| net_win_rate | 0.4555 |
| gross_profit_factor | 0.8735 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -3.5591 |
| sortino_ratio | -0.9973 |
| max_drawdown | 0.7009 |
| cagr | -0.3765 |
| net_avg_win | 51.8050 |
| net_avg_loss | -75.7958 |
| avg_hold_time_bars | 11.4835 |
| exposure | 0.2051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
