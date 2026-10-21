# EMA Hourly Continuation — SUI/USDT P21_55

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.8126 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0422 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.3944 |
| sortino_ratio | -0.4189 |
| max_drawdown | 0.4310 |
| cagr | -0.1754 |
| net_avg_win | 74.6400 |
| net_avg_loss | -95.7149 |
| avg_hold_time_bars | 9.3089 |
| exposure | 0.1849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
