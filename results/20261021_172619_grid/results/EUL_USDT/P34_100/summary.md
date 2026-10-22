# EMA Hourly Continuation — EUL/USDT P34_100

**Symbol:** EUL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6941 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -2.0922 |
| sortino_ratio | -0.5967 |
| max_drawdown | 0.5194 |
| cagr | -0.2404 |
| net_avg_win | 59.5560 |
| net_avg_loss | -77.2593 |
| avg_hold_time_bars | 13.3915 |
| exposure | 0.2441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
