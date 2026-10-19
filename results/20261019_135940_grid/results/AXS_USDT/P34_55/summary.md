# EMA Hourly Continuation — AXS/USDT P34_55

**Symbol:** AXS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 836 |
| net_profit_factor | 0.4525 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -7.7951 |
| sortino_ratio | -3.1782 |
| max_drawdown | 0.9827 |
| cagr | -0.7962 |
| net_avg_win | 22.0555 |
| net_avg_loss | -38.3238 |
| avg_hold_time_bars | 3.2201 |
| exposure | 0.1218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
