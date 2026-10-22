# EMA Hourly Continuation — BONK/USDT P20_144

**Symbol:** BONK/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.6518 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -3.0178 |
| sortino_ratio | -0.9393 |
| max_drawdown | 0.7277 |
| cagr | -0.3645 |
| net_avg_win | 54.6070 |
| net_avg_loss | -74.7894 |
| avg_hold_time_bars | 24.5688 |
| exposure | 0.5517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
