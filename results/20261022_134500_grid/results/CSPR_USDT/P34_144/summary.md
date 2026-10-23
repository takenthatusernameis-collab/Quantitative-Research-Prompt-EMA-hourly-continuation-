# EMA Hourly Continuation — CSPR/USDT P34_144

**Symbol:** CSPR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 733 |
| net_profit_factor | 0.4706 |
| net_win_rate | 0.4025 |
| gross_profit_factor | 0.7299 |
| gross_win_rate | 0.4065 |
| sharpe_ratio | -6.4411 |
| sortino_ratio | -2.4472 |
| max_drawdown | 0.9499 |
| cagr | -0.6934 |
| net_avg_win | 28.5865 |
| net_avg_loss | -40.9120 |
| avg_hold_time_bars | 12.0928 |
| exposure | 0.4029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
