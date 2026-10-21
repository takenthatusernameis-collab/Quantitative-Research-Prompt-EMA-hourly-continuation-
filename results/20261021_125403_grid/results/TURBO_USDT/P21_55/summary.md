# EMA Hourly Continuation — TURBO/USDT P21_55

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.8419 |
| net_win_rate | 0.5110 |
| gross_profit_factor | 1.0548 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -1.3442 |
| sortino_ratio | -0.4273 |
| max_drawdown | 0.4362 |
| cagr | -0.1801 |
| net_avg_win | 86.6173 |
| net_avg_loss | -107.5147 |
| avg_hold_time_bars | 8.6015 |
| exposure | 0.1919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
