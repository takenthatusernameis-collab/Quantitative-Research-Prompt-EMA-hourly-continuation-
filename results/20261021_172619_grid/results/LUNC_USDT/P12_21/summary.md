# EMA Hourly Continuation — LUNC/USDT P12_21

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.6090 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8829 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.4522 |
| sortino_ratio | -0.5555 |
| max_drawdown | 0.4789 |
| cagr | -0.2245 |
| net_avg_win | 62.8240 |
| net_avg_loss | -90.7542 |
| avg_hold_time_bars | 4.4760 |
| exposure | 0.0509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
