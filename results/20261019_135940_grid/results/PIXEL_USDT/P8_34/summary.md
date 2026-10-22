# EMA Hourly Continuation — PIXEL/USDT P8_34

**Symbol:** PIXEL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1351 |
| net_profit_factor | 0.6136 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 1.0264 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -6.7836 |
| sortino_ratio | -3.5075 |
| max_drawdown | 0.9853 |
| cagr | -0.8115 |
| net_avg_win | 25.0331 |
| net_avg_loss | -35.1201 |
| avg_hold_time_bars | 5.8764 |
| exposure | 0.3592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
