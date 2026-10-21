# EMA Hourly Continuation — PUNDIX/USDT P26_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7478 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9761 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -1.9100 |
| sortino_ratio | -0.5575 |
| max_drawdown | 0.4813 |
| cagr | -0.2278 |
| net_avg_win | 68.7377 |
| net_avg_loss | -89.3197 |
| avg_hold_time_bars | 26.2297 |
| exposure | 0.4984 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
