# EMA Hourly Continuation — SUPER/USDT P20_100

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.8324 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.1945 |
| sortino_ratio | -0.3860 |
| max_drawdown | 0.4095 |
| cagr | -0.1644 |
| net_avg_win | 69.3470 |
| net_avg_loss | -88.0543 |
| avg_hold_time_bars | 17.5474 |
| exposure | 0.4036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
