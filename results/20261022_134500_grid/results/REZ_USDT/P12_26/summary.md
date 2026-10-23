# EMA Hourly Continuation — REZ/USDT P12_26

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1287 |
| net_profit_factor | 0.5123 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.8858 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -8.8997 |
| sortino_ratio | -4.5287 |
| max_drawdown | 0.9959 |
| cagr | -0.8914 |
| net_avg_win | 18.6786 |
| net_avg_loss | -28.0865 |
| avg_hold_time_bars | 3.4709 |
| exposure | 0.2061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
