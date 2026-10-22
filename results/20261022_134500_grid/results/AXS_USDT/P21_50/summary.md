# EMA Hourly Continuation — AXS/USDT P21_50

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.5287 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9821 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -6.5260 |
| sortino_ratio | -2.7910 |
| max_drawdown | 0.9689 |
| cagr | -0.7432 |
| net_avg_win | 25.4228 |
| net_avg_loss | -41.4774 |
| avg_hold_time_bars | 4.6768 |
| exposure | 0.1951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
