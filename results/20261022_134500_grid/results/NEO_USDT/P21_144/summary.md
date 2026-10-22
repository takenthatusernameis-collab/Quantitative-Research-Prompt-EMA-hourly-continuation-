# EMA Hourly Continuation — NEO/USDT P21_144

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.6042 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -3.0655 |
| sortino_ratio | -0.9016 |
| max_drawdown | 0.6785 |
| cagr | -0.3497 |
| net_avg_win | 48.4958 |
| net_avg_loss | -73.2195 |
| avg_hold_time_bars | 29.7041 |
| exposure | 0.5887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
