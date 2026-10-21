# EMA Hourly Continuation — ONDO/USDT P12_20

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.7421 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9945 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3537 |
| sortino_ratio | -0.2856 |
| max_drawdown | 0.3223 |
| cagr | -0.1226 |
| net_avg_win | 74.6324 |
| net_avg_loss | -100.5632 |
| avg_hold_time_bars | 5.3472 |
| exposure | 0.0525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
