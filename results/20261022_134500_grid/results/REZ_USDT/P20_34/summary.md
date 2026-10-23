# EMA Hourly Continuation — REZ/USDT P20_34

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.5701 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 1.0405 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -7.9951 |
| sortino_ratio | -3.6905 |
| max_drawdown | 0.9893 |
| cagr | -0.8387 |
| net_avg_win | 27.8487 |
| net_avg_loss | -38.7981 |
| avg_hold_time_bars | 3.2237 |
| exposure | 0.1582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
