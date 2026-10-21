# EMA Hourly Continuation — BABYDOGE/USDT P34_100

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 44 |
| net_profit_factor | 0.9137 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9898 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.1670 |
| sortino_ratio | -0.0158 |
| max_drawdown | 0.0720 |
| cagr | -0.0078 |
| net_avg_win | 94.5960 |
| net_avg_loss | -103.5293 |
| avg_hold_time_bars | 23.5000 |
| exposure | 0.0468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
