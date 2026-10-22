# EMA Hourly Continuation — QNT/USDT P26_50

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1069 |
| net_profit_factor | 0.3107 |
| net_win_rate | 0.4191 |
| gross_profit_factor | 0.7409 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -10.1825 |
| sortino_ratio | -4.7273 |
| max_drawdown | 0.9977 |
| cagr | -0.9090 |
| net_avg_win | 10.0349 |
| net_avg_loss | -23.3032 |
| avg_hold_time_bars | 3.2470 |
| exposure | 0.1578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
