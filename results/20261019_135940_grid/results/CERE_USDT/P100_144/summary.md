# EMA Hourly Continuation — CERE/USDT P100_144

**Symbol:** CERE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.3657 |
| net_win_rate | 0.2935 |
| gross_profit_factor | 0.6660 |
| gross_win_rate | 0.3234 |
| sharpe_ratio | -10.5976 |
| sortino_ratio | -3.7626 |
| max_drawdown | 0.9932 |
| cagr | -0.8627 |
| net_avg_win | 32.3450 |
| net_avg_loss | -36.7529 |
| avg_hold_time_bars | 4.8789 |
| exposure | 0.1337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
