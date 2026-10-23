# EMA Hourly Continuation — EDU/USDT P89_144

**Symbol:** EDU/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.5081 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.8109 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -5.3616 |
| sortino_ratio | -1.7544 |
| max_drawdown | 0.8909 |
| cagr | -0.5763 |
| net_avg_win | 39.0876 |
| net_avg_loss | -57.6942 |
| avg_hold_time_bars | 5.4927 |
| exposure | 0.1357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
