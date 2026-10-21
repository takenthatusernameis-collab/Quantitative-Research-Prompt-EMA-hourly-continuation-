# EMA Hourly Continuation — AXL/USDT P8_200

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8083 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9485 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.2786 |
| sortino_ratio | -0.3397 |
| max_drawdown | 0.4131 |
| cagr | -0.1463 |
| net_avg_win | 81.6296 |
| net_avg_loss | -95.9117 |
| avg_hold_time_bars | 49.3438 |
| exposure | 0.7793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
