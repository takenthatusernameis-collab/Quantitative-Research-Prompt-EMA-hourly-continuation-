# EMA Hourly Continuation — POPCAT/USDT P20_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.5120 |
| net_win_rate | 0.4185 |
| gross_profit_factor | 0.6933 |
| gross_win_rate | 0.4202 |
| sharpe_ratio | -5.3872 |
| sortino_ratio | -1.9797 |
| max_drawdown | 0.8764 |
| cagr | -0.6162 |
| net_avg_win | 36.8124 |
| net_avg_loss | -51.7434 |
| avg_hold_time_bars | 13.9513 |
| exposure | 0.4385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
