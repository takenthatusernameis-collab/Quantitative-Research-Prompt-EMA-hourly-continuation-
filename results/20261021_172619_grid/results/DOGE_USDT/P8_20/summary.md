# EMA Hourly Continuation — DOGE/USDT P8_20

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9468 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -2.3556 |
| sortino_ratio | -0.6722 |
| max_drawdown | 0.5556 |
| cagr | -0.2656 |
| net_avg_win | 59.7654 |
| net_avg_loss | -84.0997 |
| avg_hold_time_bars | 5.6490 |
| exposure | 0.1017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
