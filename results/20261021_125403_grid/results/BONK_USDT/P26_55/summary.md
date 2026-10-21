# EMA Hourly Continuation — BONK/USDT P26_55

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.9015 |
| net_win_rate | 0.5328 |
| gross_profit_factor | 1.1342 |
| gross_win_rate | 0.5328 |
| sharpe_ratio | -0.6432 |
| sortino_ratio | -0.1849 |
| max_drawdown | 0.3004 |
| cagr | -0.0851 |
| net_avg_win | 86.8337 |
| net_avg_loss | -109.8583 |
| avg_hold_time_bars | 7.3838 |
| exposure | 0.1329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
