# EMA Hourly Continuation — RENDER/USDT P21_100

**Symbol:** RENDER/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.7779 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9425 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -1.7161 |
| sortino_ratio | -0.5366 |
| max_drawdown | 0.4739 |
| cagr | -0.2199 |
| net_avg_win | 72.0767 |
| net_avg_loss | -88.2807 |
| avg_hold_time_bars | 16.2995 |
| exposure | 0.3562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
