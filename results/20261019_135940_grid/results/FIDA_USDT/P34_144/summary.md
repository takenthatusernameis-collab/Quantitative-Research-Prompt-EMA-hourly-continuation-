# EMA Hourly Continuation — FIDA/USDT P34_144

**Symbol:** FIDA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6492 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9497 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -3.1570 |
| sortino_ratio | -1.0158 |
| max_drawdown | 0.7056 |
| cagr | -0.3774 |
| net_avg_win | 52.2537 |
| net_avg_loss | -73.6329 |
| avg_hold_time_bars | 17.2727 |
| exposure | 0.4041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
