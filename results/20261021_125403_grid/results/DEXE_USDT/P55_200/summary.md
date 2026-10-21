# EMA Hourly Continuation — DEXE/USDT P55_200

**Symbol:** DEXE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.9677 |
| net_win_rate | 0.5442 |
| gross_profit_factor | 1.1682 |
| gross_win_rate | 0.5442 |
| sharpe_ratio | -0.0872 |
| sortino_ratio | -0.0189 |
| max_drawdown | 0.2379 |
| cagr | -0.0126 |
| net_avg_win | 76.6059 |
| net_avg_loss | -94.5342 |
| avg_hold_time_bars | 48.3850 |
| exposure | 0.4970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
