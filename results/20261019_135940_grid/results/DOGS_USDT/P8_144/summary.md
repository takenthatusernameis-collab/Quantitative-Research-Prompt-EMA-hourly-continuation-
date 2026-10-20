# EMA Hourly Continuation — DOGS/USDT P8_144

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6258 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8620 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -3.3991 |
| sortino_ratio | -1.1054 |
| max_drawdown | 0.6922 |
| cagr | -0.4084 |
| net_avg_win | 53.3850 |
| net_avg_loss | -74.1234 |
| avg_hold_time_bars | 30.3026 |
| exposure | 0.7331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
