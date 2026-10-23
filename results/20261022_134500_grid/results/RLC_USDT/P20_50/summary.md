# EMA Hourly Continuation — RLC/USDT P20_50

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 972 |
| net_profit_factor | 0.5264 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9571 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -6.5487 |
| sortino_ratio | -2.8725 |
| max_drawdown | 0.9721 |
| cagr | -0.7540 |
| net_avg_win | 23.6047 |
| net_avg_loss | -39.7900 |
| avg_hold_time_bars | 4.9198 |
| exposure | 0.2174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
