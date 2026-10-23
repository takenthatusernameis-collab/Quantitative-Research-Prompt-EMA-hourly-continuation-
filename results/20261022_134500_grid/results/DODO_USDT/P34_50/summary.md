# EMA Hourly Continuation — DODO/USDT P34_50

**Symbol:** DODO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.4546 |
| net_win_rate | 0.4252 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -9.1120 |
| sortino_ratio | -4.0438 |
| max_drawdown | 0.9943 |
| cagr | -0.8678 |
| net_avg_win | 19.8226 |
| net_avg_loss | -32.2568 |
| avg_hold_time_bars | 2.8006 |
| exposure | 0.1246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
