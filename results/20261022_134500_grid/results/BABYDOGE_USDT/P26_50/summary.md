# EMA Hourly Continuation — BABYDOGE/USDT P26_50

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 27 |
| net_profit_factor | 1.7955 |
| net_win_rate | 0.6667 |
| gross_profit_factor | 1.9742 |
| gross_win_rate | 0.6667 |
| sharpe_ratio | 0.9426 |
| sortino_ratio | 0.0755 |
| max_drawdown | 0.0316 |
| cagr | 0.0305 |
| net_avg_win | 98.8020 |
| net_avg_loss | -110.0561 |
| avg_hold_time_bars | 12.8148 |
| exposure | 0.0157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
