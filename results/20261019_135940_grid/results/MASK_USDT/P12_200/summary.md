# EMA Hourly Continuation — MASK/USDT P12_200

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.4679 |
| net_win_rate | 0.4217 |
| gross_profit_factor | 0.7315 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -4.5331 |
| sortino_ratio | -1.2964 |
| max_drawdown | 0.8030 |
| cagr | -0.4690 |
| net_avg_win | 40.0025 |
| net_avg_loss | -62.3349 |
| avg_hold_time_bars | 38.3566 |
| exposure | 0.7235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
