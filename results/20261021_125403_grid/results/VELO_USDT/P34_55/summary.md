# EMA Hourly Continuation — VELO/USDT P34_55

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7572 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.3797 |
| sortino_ratio | -0.3255 |
| max_drawdown | 0.3398 |
| cagr | -0.1386 |
| net_avg_win | 72.1575 |
| net_avg_loss | -94.6004 |
| avg_hold_time_bars | 6.8044 |
| exposure | 0.0838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
