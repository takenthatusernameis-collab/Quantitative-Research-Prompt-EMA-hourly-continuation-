# EMA Hourly Continuation — ETC/USDT P8_144

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.4901 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8192 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -4.5769 |
| sortino_ratio | -1.4252 |
| max_drawdown | 0.8383 |
| cagr | -0.4986 |
| net_avg_win | 35.9714 |
| net_avg_loss | -59.8036 |
| avg_hold_time_bars | 33.9082 |
| exposure | 0.7552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
