# EMA Hourly Continuation — ADA/USDT P12_20

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.9414 |
| net_win_rate | 0.5766 |
| gross_profit_factor | 1.3504 |
| gross_win_rate | 0.5766 |
| sharpe_ratio | -0.2412 |
| sortino_ratio | -0.0526 |
| max_drawdown | 0.2080 |
| cagr | -0.0266 |
| net_avg_win | 82.2909 |
| net_avg_loss | -119.0312 |
| avg_hold_time_bars | 4.5180 |
| exposure | 0.0456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
