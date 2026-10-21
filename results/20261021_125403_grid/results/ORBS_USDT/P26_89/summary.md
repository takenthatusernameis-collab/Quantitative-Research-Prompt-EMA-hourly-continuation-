# EMA Hourly Continuation — ORBS/USDT P26_89

**Symbol:** ORBS/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7047 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9740 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -2.9356 |
| sortino_ratio | -0.9501 |
| max_drawdown | 0.7013 |
| cagr | -0.3531 |
| net_avg_win | 64.5213 |
| net_avg_loss | -84.3542 |
| avg_hold_time_bars | 14.4795 |
| exposure | 0.3376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
