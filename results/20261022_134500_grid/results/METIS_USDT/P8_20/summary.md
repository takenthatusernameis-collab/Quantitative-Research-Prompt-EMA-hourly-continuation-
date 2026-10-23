# EMA Hourly Continuation — METIS/USDT P8_20

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1707 |
| net_profit_factor | 0.3994 |
| net_win_rate | 0.4271 |
| gross_profit_factor | 0.8916 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -11.8302 |
| sortino_ratio | -6.9018 |
| max_drawdown | 0.9998 |
| cagr | -0.9684 |
| net_avg_win | 9.1214 |
| net_avg_loss | -17.0223 |
| avg_hold_time_bars | 2.9660 |
| exposure | 0.2301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
