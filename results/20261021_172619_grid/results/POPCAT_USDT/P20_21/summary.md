# EMA Hourly Continuation — POPCAT/USDT P20_21

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.5724 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.7613 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -2.3668 |
| sortino_ratio | -0.4455 |
| max_drawdown | 0.3681 |
| cagr | -0.1858 |
| net_avg_win | 73.8665 |
| net_avg_loss | -97.5394 |
| avg_hold_time_bars | 4.6159 |
| exposure | 0.0368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
