# EMA Hourly Continuation — NEO/USDT P21_34

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1154 |
| net_profit_factor | 0.2481 |
| net_win_rate | 0.3700 |
| gross_profit_factor | 0.6908 |
| gross_win_rate | 0.4099 |
| sharpe_ratio | -13.2147 |
| sortino_ratio | -6.4806 |
| max_drawdown | 0.9998 |
| cagr | -0.9648 |
| net_avg_win | 7.7246 |
| net_avg_loss | -18.2891 |
| avg_hold_time_bars | 2.7374 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
