# EMA Hourly Continuation — SAND/USDT P100_144

**Symbol:** SAND/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.5856 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8180 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -2.5043 |
| sortino_ratio | -0.5313 |
| max_drawdown | 0.4584 |
| cagr | -0.2167 |
| net_avg_win | 65.4431 |
| net_avg_loss | -90.6808 |
| avg_hold_time_bars | 5.4434 |
| exposure | 0.0547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
