# EMA Hourly Continuation — DOGS/USDT P100_144

**Symbol:** DOGS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.5190 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -4.7889 |
| sortino_ratio | -1.5293 |
| max_drawdown | 0.8045 |
| cagr | -0.5232 |
| net_avg_win | 43.4307 |
| net_avg_loss | -69.9065 |
| avg_hold_time_bars | 3.8644 |
| exposure | 0.0892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
