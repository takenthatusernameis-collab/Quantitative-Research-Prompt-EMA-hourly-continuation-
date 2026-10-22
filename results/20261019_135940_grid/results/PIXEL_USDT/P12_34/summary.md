# EMA Hourly Continuation — PIXEL/USDT P12_34

**Symbol:** PIXEL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1258 |
| net_profit_factor | 0.5470 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.9487 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -7.6305 |
| sortino_ratio | -3.7992 |
| max_drawdown | 0.9904 |
| cagr | -0.8412 |
| net_avg_win | 21.0189 |
| net_avg_loss | -31.7321 |
| avg_hold_time_bars | 4.9340 |
| exposure | 0.2809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
