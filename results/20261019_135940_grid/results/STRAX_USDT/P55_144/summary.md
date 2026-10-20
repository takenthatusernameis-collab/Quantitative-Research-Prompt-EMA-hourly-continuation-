# EMA Hourly Continuation — STRAX/USDT P55_144

**Symbol:** STRAX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.5169 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.8297 |
| gross_win_rate | 0.4304 |
| sharpe_ratio | -5.8348 |
| sortino_ratio | -1.9500 |
| max_drawdown | 0.9020 |
| cagr | -0.6056 |
| net_avg_win | 41.6043 |
| net_avg_loss | -58.1690 |
| avg_hold_time_bars | 10.0072 |
| exposure | 0.2530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
