# EMA Hourly Continuation — AERO/USDT P8_26

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.8398 |
| net_win_rate | 0.5209 |
| gross_profit_factor | 1.0744 |
| gross_win_rate | 0.5209 |
| sharpe_ratio | -1.3934 |
| sortino_ratio | -0.5190 |
| max_drawdown | 0.4986 |
| cagr | -0.2144 |
| net_avg_win | 68.2434 |
| net_avg_loss | -88.3548 |
| avg_hold_time_bars | 6.1582 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
