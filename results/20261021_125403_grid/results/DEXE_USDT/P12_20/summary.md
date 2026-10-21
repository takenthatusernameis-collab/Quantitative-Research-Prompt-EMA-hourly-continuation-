# EMA Hourly Continuation — DEXE/USDT P12_20

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.5823 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.8579 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -2.5958 |
| sortino_ratio | -0.6534 |
| max_drawdown | 0.5391 |
| cagr | -0.2600 |
| net_avg_win | 50.3129 |
| net_avg_loss | -78.4054 |
| avg_hold_time_bars | 11.7702 |
| exposure | 0.1653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
