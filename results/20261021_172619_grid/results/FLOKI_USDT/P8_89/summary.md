# EMA Hourly Continuation — FLOKI/USDT P8_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.7957 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9560 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -1.7143 |
| sortino_ratio | -0.5726 |
| max_drawdown | 0.4983 |
| cagr | -0.2327 |
| net_avg_win | 70.6073 |
| net_avg_loss | -85.2369 |
| avg_hold_time_bars | 24.4351 |
| exposure | 0.6075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
