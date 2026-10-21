# EMA Hourly Continuation — IOTX/USDT P55_144

**Symbol:** IOTX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.6863 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.8841 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -2.0912 |
| sortino_ratio | -0.5650 |
| max_drawdown | 0.4835 |
| cagr | -0.2287 |
| net_avg_win | 61.2834 |
| net_avg_loss | -81.2261 |
| avg_hold_time_bars | 15.6323 |
| exposure | 0.2551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
