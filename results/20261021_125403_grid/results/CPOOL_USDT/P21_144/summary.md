# EMA Hourly Continuation — CPOOL/USDT P21_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.8767 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0133 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -0.8634 |
| sortino_ratio | -0.2612 |
| max_drawdown | 0.3492 |
| cagr | -0.1171 |
| net_avg_win | 84.4660 |
| net_avg_loss | -98.5293 |
| avg_hold_time_bars | 20.8770 |
| exposure | 0.4242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
