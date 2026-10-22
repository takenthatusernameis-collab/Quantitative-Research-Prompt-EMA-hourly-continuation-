# EMA Hourly Continuation — RENDER/USDT P26_144

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7477 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0150 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -2.0623 |
| sortino_ratio | -0.6263 |
| max_drawdown | 0.5252 |
| cagr | -0.2569 |
| net_avg_win | 70.9400 |
| net_avg_loss | -94.8735 |
| avg_hold_time_bars | 22.9066 |
| exposure | 0.4788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
