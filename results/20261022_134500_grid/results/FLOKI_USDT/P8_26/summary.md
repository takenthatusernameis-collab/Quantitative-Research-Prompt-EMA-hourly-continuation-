# EMA Hourly Continuation — FLOKI/USDT P8_26

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1625 |
| net_profit_factor | 0.3894 |
| net_win_rate | 0.4148 |
| gross_profit_factor | 0.6956 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -11.5800 |
| sortino_ratio | -6.5364 |
| max_drawdown | 0.9998 |
| cagr | -0.9639 |
| net_avg_win | 9.4614 |
| net_avg_loss | -17.2183 |
| avg_hold_time_bars | 3.5292 |
| exposure | 0.2607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
