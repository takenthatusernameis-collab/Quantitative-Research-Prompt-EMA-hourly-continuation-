# EMA Hourly Continuation — SSV/USDT P21_34

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1220 |
| net_profit_factor | 0.3947 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.7710 |
| gross_win_rate | 0.4246 |
| sharpe_ratio | -10.9070 |
| sortino_ratio | -5.4088 |
| max_drawdown | 0.9989 |
| cagr | -0.9329 |
| net_avg_win | 13.1845 |
| net_avg_loss | -22.7303 |
| avg_hold_time_bars | 2.7311 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
