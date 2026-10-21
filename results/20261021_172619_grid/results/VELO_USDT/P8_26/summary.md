# EMA Hourly Continuation — VELO/USDT P8_26

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.8396 |
| net_win_rate | 0.5190 |
| gross_profit_factor | 1.0558 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -1.2022 |
| sortino_ratio | -0.4162 |
| max_drawdown | 0.4083 |
| cagr | -0.1763 |
| net_avg_win | 67.2643 |
| net_avg_loss | -86.4583 |
| avg_hold_time_bars | 6.8495 |
| exposure | 0.1800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
