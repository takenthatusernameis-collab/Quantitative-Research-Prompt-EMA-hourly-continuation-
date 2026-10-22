# EMA Hourly Continuation — XMR/USDT P8_34

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1728 |
| net_profit_factor | 0.2271 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.5844 |
| gross_win_rate | 0.4115 |
| sharpe_ratio | -14.1706 |
| sortino_ratio | -8.3293 |
| max_drawdown | 1.0000 |
| cagr | -0.9863 |
| net_avg_win | 4.2780 |
| net_avg_loss | -12.4292 |
| avg_hold_time_bars | 3.8258 |
| exposure | 0.3005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
