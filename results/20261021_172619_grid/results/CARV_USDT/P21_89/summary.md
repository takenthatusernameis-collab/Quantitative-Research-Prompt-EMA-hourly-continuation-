# EMA Hourly Continuation — CARV/USDT P21_89

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7653 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9664 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.9769 |
| sortino_ratio | -0.6276 |
| max_drawdown | 0.4991 |
| cagr | -0.2513 |
| net_avg_win | 74.2617 |
| net_avg_loss | -92.7543 |
| avg_hold_time_bars | 16.5063 |
| exposure | 0.3706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
