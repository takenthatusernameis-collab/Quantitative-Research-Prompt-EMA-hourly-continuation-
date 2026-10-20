# EMA Hourly Continuation — SUPER/USDT P8_12

**Symbol:** SUPER/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1745 |
| net_profit_factor | 0.2507 |
| net_win_rate | 0.3954 |
| gross_profit_factor | 0.8041 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -15.1589 |
| sortino_ratio | -9.0384 |
| max_drawdown | 1.0000 |
| cagr | -0.9912 |
| net_avg_win | 4.8502 |
| net_avg_loss | -12.6508 |
| avg_hold_time_bars | 2.0527 |
| exposure | 0.1628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
