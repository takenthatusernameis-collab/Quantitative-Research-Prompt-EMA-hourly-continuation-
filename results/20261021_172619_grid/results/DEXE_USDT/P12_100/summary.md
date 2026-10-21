# EMA Hourly Continuation — DEXE/USDT P12_100

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.9157 |
| net_win_rate | 0.5286 |
| gross_profit_factor | 1.0995 |
| gross_win_rate | 0.5286 |
| sharpe_ratio | -0.4613 |
| sortino_ratio | -0.1362 |
| max_drawdown | 0.2819 |
| cagr | -0.0658 |
| net_avg_win | 76.8581 |
| net_avg_loss | -94.1112 |
| avg_hold_time_bars | 33.6000 |
| exposure | 0.6415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
