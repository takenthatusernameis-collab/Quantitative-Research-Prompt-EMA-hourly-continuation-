# EMA Hourly Continuation — DEXE/USDT P50_100

**Symbol:** DEXE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7823 |
| net_win_rate | 0.5110 |
| gross_profit_factor | 1.0129 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -1.1928 |
| sortino_ratio | -0.3056 |
| max_drawdown | 0.3726 |
| cagr | -0.1316 |
| net_avg_win | 65.7941 |
| net_avg_loss | -87.8758 |
| avg_hold_time_bars | 21.9875 |
| exposure | 0.3188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
