# EMA Hourly Continuation — AXL/USDT P26_144

**Symbol:** AXL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.7940 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9589 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -1.7312 |
| sortino_ratio | -0.5270 |
| max_drawdown | 0.4896 |
| cagr | -0.2169 |
| net_avg_win | 79.9264 |
| net_avg_loss | -94.6900 |
| avg_hold_time_bars | 20.8865 |
| exposure | 0.4329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
