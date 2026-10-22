# EMA Hourly Continuation — CATI/USDT P89_144

**Symbol:** CATI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.5572 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7263 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -2.7813 |
| sortino_ratio | -0.6153 |
| max_drawdown | 0.4519 |
| cagr | -0.2475 |
| net_avg_win | 65.4042 |
| net_avg_loss | -87.0180 |
| avg_hold_time_bars | 10.6535 |
| exposure | 0.1180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
