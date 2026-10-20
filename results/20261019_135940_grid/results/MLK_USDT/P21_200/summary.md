# EMA Hourly Continuation — MLK/USDT P21_200

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.4285 |
| net_win_rate | 0.3380 |
| gross_profit_factor | 0.6339 |
| gross_win_rate | 0.3411 |
| sharpe_ratio | -8.1981 |
| sortino_ratio | -2.9419 |
| max_drawdown | 0.9741 |
| cagr | -0.7621 |
| net_avg_win | 33.4690 |
| net_avg_loss | -39.8805 |
| avg_hold_time_bars | 19.1566 |
| exposure | 0.5592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
