# EMA Hourly Continuation — ETN/USDT P34_200

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.5473 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.7949 |
| gross_win_rate | 0.4340 |
| sharpe_ratio | -5.0131 |
| sortino_ratio | -1.6718 |
| max_drawdown | 0.8229 |
| cagr | -0.5548 |
| net_avg_win | 48.6894 |
| net_avg_loss | -65.9051 |
| avg_hold_time_bars | 15.8155 |
| exposure | 0.4098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
