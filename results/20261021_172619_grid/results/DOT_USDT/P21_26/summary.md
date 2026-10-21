# EMA Hourly Continuation — DOT/USDT P21_26

**Symbol:** DOT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 129 |
| net_profit_factor | 0.7034 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9922 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.2659 |
| sortino_ratio | -0.2066 |
| max_drawdown | 0.2769 |
| cagr | -0.0897 |
| net_avg_win | 77.8801 |
| net_avg_loss | -109.0145 |
| avg_hold_time_bars | 4.9767 |
| exposure | 0.0292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
