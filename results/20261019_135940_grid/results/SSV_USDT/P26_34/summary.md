# EMA Hourly Continuation — SSV/USDT P26_34

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1160 |
| net_profit_factor | 0.3273 |
| net_win_rate | 0.3931 |
| gross_profit_factor | 0.7392 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -11.9986 |
| sortino_ratio | -5.8353 |
| max_drawdown | 0.9995 |
| cagr | -0.9508 |
| net_avg_win | 10.6664 |
| net_avg_loss | -21.1063 |
| avg_hold_time_bars | 2.3207 |
| exposure | 0.1218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
