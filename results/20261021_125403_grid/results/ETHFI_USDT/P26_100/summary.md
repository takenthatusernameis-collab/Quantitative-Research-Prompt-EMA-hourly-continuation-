# EMA Hourly Continuation — ETHFI/USDT P26_100

**Symbol:** ETHFI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.8667 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0312 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.0505 |
| sortino_ratio | -0.3234 |
| max_drawdown | 0.4236 |
| cagr | -0.1409 |
| net_avg_win | 88.5127 |
| net_avg_loss | -104.3636 |
| avg_hold_time_bars | 16.4165 |
| exposure | 0.3440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
