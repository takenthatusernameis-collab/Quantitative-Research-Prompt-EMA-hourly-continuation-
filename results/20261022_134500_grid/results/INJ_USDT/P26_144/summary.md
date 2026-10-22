# EMA Hourly Continuation — INJ/USDT P26_144

**Symbol:** INJ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6344 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -3.2311 |
| sortino_ratio | -1.0075 |
| max_drawdown | 0.7153 |
| cagr | -0.3879 |
| net_avg_win | 51.8761 |
| net_avg_loss | -73.4069 |
| avg_hold_time_bars | 20.5250 |
| exposure | 0.4674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
