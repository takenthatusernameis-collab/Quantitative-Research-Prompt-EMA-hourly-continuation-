# EMA Hourly Continuation — ASTR/USDT P8_26

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 820 |
| net_profit_factor | 0.6462 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9422 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -4.1760 |
| sortino_ratio | -1.7051 |
| max_drawdown | 0.8639 |
| cagr | -0.5447 |
| net_avg_win | 39.6881 |
| net_avg_loss | -57.6410 |
| avg_hold_time_bars | 6.6707 |
| exposure | 0.2475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
