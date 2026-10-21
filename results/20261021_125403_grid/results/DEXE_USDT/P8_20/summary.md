# EMA Hourly Continuation — DEXE/USDT P8_20

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.6864 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 0.9722 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -2.1961 |
| sortino_ratio | -0.7152 |
| max_drawdown | 0.5792 |
| cagr | -0.2805 |
| net_avg_win | 47.1753 |
| net_avg_loss | -70.9038 |
| avg_hold_time_bars | 9.9280 |
| exposure | 0.2320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
