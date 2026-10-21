# EMA Hourly Continuation — MANA/USDT P20_144

**Symbol:** MANA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.8338 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0138 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.0591 |
| sortino_ratio | -0.2861 |
| max_drawdown | 0.3271 |
| cagr | -0.1251 |
| net_avg_win | 79.4719 |
| net_avg_loss | -97.4764 |
| avg_hold_time_bars | 34.6517 |
| exposure | 0.5607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
