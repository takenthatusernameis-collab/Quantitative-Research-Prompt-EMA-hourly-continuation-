# EMA Hourly Continuation — FLR/USDT P20_34

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1333 |
| net_profit_factor | 0.3550 |
| net_win_rate | 0.3623 |
| gross_profit_factor | 0.8862 |
| gross_win_rate | 0.4021 |
| sharpe_ratio | -14.5403 |
| sortino_ratio | -7.6458 |
| max_drawdown | 1.0000 |
| cagr | -0.9815 |
| net_avg_win | 11.3970 |
| net_avg_loss | -18.2404 |
| avg_hold_time_bars | 2.5911 |
| exposure | 0.1570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
