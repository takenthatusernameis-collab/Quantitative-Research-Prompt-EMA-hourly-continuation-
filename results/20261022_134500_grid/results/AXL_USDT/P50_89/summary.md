# EMA Hourly Continuation — AXL/USDT P50_89

**Symbol:** AXL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.4930 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.8176 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -6.2912 |
| sortino_ratio | -2.3960 |
| max_drawdown | 0.9470 |
| cagr | -0.6855 |
| net_avg_win | 29.3844 |
| net_avg_loss | -44.3156 |
| avg_hold_time_bars | 4.9632 |
| exposure | 0.1648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
