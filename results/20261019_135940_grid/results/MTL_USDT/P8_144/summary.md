# EMA Hourly Continuation — MTL/USDT P8_144

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.7301 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0736 |
| gross_win_rate | 0.5128 |
| sharpe_ratio | -2.0876 |
| sortino_ratio | -0.5844 |
| max_drawdown | 0.5264 |
| cagr | -0.2424 |
| net_avg_win | 69.4905 |
| net_avg_loss | -95.1832 |
| avg_hold_time_bars | 45.1990 |
| exposure | 0.8018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
