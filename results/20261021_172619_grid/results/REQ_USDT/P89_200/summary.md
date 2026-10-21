# EMA Hourly Continuation — REQ/USDT P89_200

**Symbol:** REQ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.5072 |
| net_win_rate | 0.3937 |
| gross_profit_factor | 0.7512 |
| gross_win_rate | 0.3966 |
| sharpe_ratio | -4.7471 |
| sortino_ratio | -1.2640 |
| max_drawdown | 0.7843 |
| cagr | -0.4454 |
| net_avg_win | 58.0341 |
| net_avg_loss | -74.2889 |
| avg_hold_time_bars | 12.0891 |
| exposure | 0.1912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
