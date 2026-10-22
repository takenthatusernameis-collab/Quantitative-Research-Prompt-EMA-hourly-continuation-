# EMA Hourly Continuation — ANYONE/USDT P34_50

**Symbol:** ANYONE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.5177 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.6665 |
| gross_win_rate | 0.3976 |
| sharpe_ratio | -3.5714 |
| sortino_ratio | -0.8422 |
| max_drawdown | 0.5934 |
| cagr | -0.3284 |
| net_avg_win | 63.0370 |
| net_avg_loss | -80.3775 |
| avg_hold_time_bars | 5.2087 |
| exposure | 0.0669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
