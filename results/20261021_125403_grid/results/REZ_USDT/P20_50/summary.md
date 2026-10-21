# EMA Hourly Continuation — REZ/USDT P20_50

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.7876 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9931 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -2.0317 |
| sortino_ratio | -0.6773 |
| max_drawdown | 0.6162 |
| cagr | -0.2672 |
| net_avg_win | 75.6509 |
| net_avg_loss | -92.8781 |
| avg_hold_time_bars | 7.7981 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
