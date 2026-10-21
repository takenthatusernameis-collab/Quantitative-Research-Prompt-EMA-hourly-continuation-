# EMA Hourly Continuation — XTZ/USDT P26_34

**Symbol:** XTZ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.6215 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9915 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -2.5398 |
| sortino_ratio | -0.5941 |
| max_drawdown | 0.5055 |
| cagr | -0.2378 |
| net_avg_win | 62.9375 |
| net_avg_loss | -97.4847 |
| avg_hold_time_bars | 4.6388 |
| exposure | 0.0555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
