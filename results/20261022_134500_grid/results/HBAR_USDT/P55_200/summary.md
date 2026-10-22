# EMA Hourly Continuation — HBAR/USDT P55_200

**Symbol:** HBAR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6747 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 1.0034 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.3702 |
| sortino_ratio | -0.6231 |
| max_drawdown | 0.5437 |
| cagr | -0.2594 |
| net_avg_win | 62.7529 |
| net_avg_loss | -91.9614 |
| avg_hold_time_bars | 22.5966 |
| exposure | 0.3615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
