# EMA Hourly Continuation — XPR/USDT P21_100

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.4610 |
| net_win_rate | 0.4189 |
| gross_profit_factor | 0.8008 |
| gross_win_rate | 0.4272 |
| sharpe_ratio | -7.0874 |
| sortino_ratio | -2.6550 |
| max_drawdown | 0.9672 |
| cagr | -0.7407 |
| net_avg_win | 27.3622 |
| net_avg_loss | -42.7830 |
| avg_hold_time_bars | 9.9237 |
| exposure | 0.3252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
