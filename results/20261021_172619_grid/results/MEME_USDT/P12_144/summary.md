# EMA Hourly Continuation — MEME/USDT P12_144

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.8109 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -1.2392 |
| sortino_ratio | -0.3354 |
| max_drawdown | 0.3697 |
| cagr | -0.1442 |
| net_avg_win | 77.9988 |
| net_avg_loss | -94.0689 |
| avg_hold_time_bars | 42.1139 |
| exposure | 0.6891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
