# EMA Hourly Continuation — PUNDIX/USDT P8_20

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.5162 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.7915 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -5.9291 |
| sortino_ratio | -2.2920 |
| max_drawdown | 0.9317 |
| cagr | -0.6527 |
| net_avg_win | 31.1001 |
| net_avg_loss | -46.9889 |
| avg_hold_time_bars | 6.0316 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
