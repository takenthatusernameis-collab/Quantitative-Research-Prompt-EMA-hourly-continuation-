# EMA Hourly Continuation — ZIL/USDT P89_200

**Symbol:** ZIL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5914 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -3.1993 |
| sortino_ratio | -0.9063 |
| max_drawdown | 0.6755 |
| cagr | -0.3564 |
| net_avg_win | 48.4351 |
| net_avg_loss | -79.1322 |
| avg_hold_time_bars | 10.9509 |
| exposure | 0.2026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
