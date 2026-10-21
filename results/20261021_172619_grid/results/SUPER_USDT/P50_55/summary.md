# EMA Hourly Continuation — SUPER/USDT P50_55

**Symbol:** SUPER/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.8392 |
| net_win_rate | 0.5588 |
| gross_profit_factor | 1.2866 |
| gross_win_rate | 0.5662 |
| sharpe_ratio | -0.6216 |
| sortino_ratio | -0.1047 |
| max_drawdown | 0.2502 |
| cagr | -0.0480 |
| net_avg_win | 79.7241 |
| net_avg_loss | -120.3375 |
| avg_hold_time_bars | 7.0588 |
| exposure | 0.0436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
