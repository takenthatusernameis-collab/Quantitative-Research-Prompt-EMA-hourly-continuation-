# EMA Hourly Continuation — DUSK/USDT P12_89

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7273 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8664 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -2.5099 |
| sortino_ratio | -0.8342 |
| max_drawdown | 0.6541 |
| cagr | -0.3196 |
| net_avg_win | 65.6030 |
| net_avg_loss | -76.5325 |
| avg_hold_time_bars | 21.1093 |
| exposure | 0.5268 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
