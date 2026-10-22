# EMA Hourly Continuation — FLOKI/USDT P21_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 737 |
| net_profit_factor | 0.6314 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9375 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -4.2046 |
| sortino_ratio | -1.6091 |
| max_drawdown | 0.8648 |
| cagr | -0.5345 |
| net_avg_win | 41.7636 |
| net_avg_loss | -59.8241 |
| avg_hold_time_bars | 12.0909 |
| exposure | 0.4050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
