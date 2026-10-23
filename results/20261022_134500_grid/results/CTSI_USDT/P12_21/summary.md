# EMA Hourly Continuation — CTSI/USDT P12_21

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1367 |
| net_profit_factor | 0.3181 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.8701 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -11.1632 |
| sortino_ratio | -5.8818 |
| max_drawdown | 0.9993 |
| cagr | -0.9460 |
| net_avg_win | 7.9691 |
| net_avg_loss | -18.7408 |
| avg_hold_time_bars | 2.9759 |
| exposure | 0.1849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
