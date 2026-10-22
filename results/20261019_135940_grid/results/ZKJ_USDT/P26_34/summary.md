# EMA Hourly Continuation — ZKJ/USDT P26_34

**Symbol:** ZKJ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1297 |
| net_profit_factor | 0.1262 |
| net_win_rate | 0.2336 |
| gross_profit_factor | 0.4111 |
| gross_win_rate | 0.3462 |
| sharpe_ratio | -20.1745 |
| sortino_ratio | -11.2282 |
| max_drawdown | 1.0000 |
| cagr | -0.9980 |
| net_avg_win | 4.7677 |
| net_avg_loss | -11.5137 |
| avg_hold_time_bars | 3.0054 |
| exposure | 0.1772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
