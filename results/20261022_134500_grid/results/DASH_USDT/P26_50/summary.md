# EMA Hourly Continuation — DASH/USDT P26_50

**Symbol:** DASH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.3577 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -8.5049 |
| sortino_ratio | -3.7191 |
| max_drawdown | 0.9915 |
| cagr | -0.8502 |
| net_avg_win | 12.8391 |
| net_avg_loss | -28.5848 |
| avg_hold_time_bars | 3.7577 |
| exposure | 0.1657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
