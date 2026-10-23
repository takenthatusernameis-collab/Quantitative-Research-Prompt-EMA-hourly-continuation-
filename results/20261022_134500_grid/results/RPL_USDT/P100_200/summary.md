# EMA Hourly Continuation — RPL/USDT P100_200

**Symbol:** RPL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.7543 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0485 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.7953 |
| sortino_ratio | -0.4851 |
| max_drawdown | 0.4326 |
| cagr | -0.1997 |
| net_avg_win | 73.3010 |
| net_avg_loss | -98.8290 |
| avg_hold_time_bars | 10.0308 |
| exposure | 0.1621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
