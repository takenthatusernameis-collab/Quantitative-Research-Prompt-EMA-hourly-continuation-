# EMA Hourly Continuation — MTL/USDT P12_34

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 762 |
| net_profit_factor | 0.6245 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9415 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -4.8263 |
| sortino_ratio | -1.8989 |
| max_drawdown | 0.8999 |
| cagr | -0.5865 |
| net_avg_win | 41.4558 |
| net_avg_loss | -58.8199 |
| avg_hold_time_bars | 7.3570 |
| exposure | 0.2537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
