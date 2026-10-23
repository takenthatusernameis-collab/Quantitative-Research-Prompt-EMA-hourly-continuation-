# EMA Hourly Continuation — AXL/USDT P8_89

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 843 |
| net_profit_factor | 0.5730 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8263 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -5.7059 |
| sortino_ratio | -2.3137 |
| max_drawdown | 0.9424 |
| cagr | -0.6722 |
| net_avg_win | 34.7534 |
| net_avg_loss | -45.8662 |
| avg_hold_time_bars | 16.2135 |
| exposure | 0.6185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
