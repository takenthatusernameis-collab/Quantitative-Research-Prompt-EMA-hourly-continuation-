# EMA Hourly Continuation — POKT/USDT P12_55

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.6264 |
| net_win_rate | 0.4188 |
| gross_profit_factor | 0.7982 |
| gross_win_rate | 0.4218 |
| sharpe_ratio | -4.4935 |
| sortino_ratio | -1.6397 |
| max_drawdown | 0.8563 |
| cagr | -0.5314 |
| net_avg_win | 50.8535 |
| net_avg_loss | -58.4928 |
| avg_hold_time_bars | 10.7779 |
| exposure | 0.3273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
