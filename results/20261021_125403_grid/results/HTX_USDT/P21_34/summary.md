# EMA Hourly Continuation — HTX/USDT P21_34

**Symbol:** HTX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.2770 |
| net_win_rate | 0.3185 |
| gross_profit_factor | 0.5363 |
| gross_win_rate | 0.3284 |
| sharpe_ratio | -8.2136 |
| sortino_ratio | -2.4344 |
| max_drawdown | 0.9471 |
| cagr | -0.6882 |
| net_avg_win | 28.1318 |
| net_avg_loss | -47.4643 |
| avg_hold_time_bars | 6.2173 |
| exposure | 0.1139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
