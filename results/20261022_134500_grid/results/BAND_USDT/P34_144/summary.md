# EMA Hourly Continuation — BAND/USDT P34_144

**Symbol:** BAND/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6056 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -3.1350 |
| sortino_ratio | -0.9321 |
| max_drawdown | 0.6766 |
| cagr | -0.3540 |
| net_avg_win | 49.3118 |
| net_avg_loss | -71.4610 |
| avg_hold_time_bars | 20.4270 |
| exposure | 0.4113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
