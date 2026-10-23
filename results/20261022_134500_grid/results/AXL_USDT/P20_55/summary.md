# EMA Hourly Continuation — AXL/USDT P20_55

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1027 |
| net_profit_factor | 0.5428 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4304 |
| sharpe_ratio | -7.6081 |
| sortino_ratio | -3.4217 |
| max_drawdown | 0.9850 |
| cagr | -0.8083 |
| net_avg_win | 27.1139 |
| net_avg_loss | -36.1261 |
| avg_hold_time_bars | 5.4771 |
| exposure | 0.2545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
