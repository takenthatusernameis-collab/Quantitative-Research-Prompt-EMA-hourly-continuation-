# EMA Hourly Continuation — ASTR/USDT P34_144

**Symbol:** ASTR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7759 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0120 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.5638 |
| sortino_ratio | -0.4396 |
| max_drawdown | 0.4501 |
| cagr | -0.1836 |
| net_avg_win | 71.1091 |
| net_avg_loss | -93.0800 |
| avg_hold_time_bars | 22.7700 |
| exposure | 0.3988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
