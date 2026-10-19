# EMA Hourly Continuation — FLOKI/USDT P8_12

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1893 |
| net_profit_factor | 0.2232 |
| net_win_rate | 0.3481 |
| gross_profit_factor | 0.5364 |
| gross_win_rate | 0.3941 |
| sharpe_ratio | -18.7135 |
| sortino_ratio | -11.7830 |
| max_drawdown | 1.0000 |
| cagr | -0.9981 |
| net_avg_win | 4.3603 |
| net_avg_loss | -10.4323 |
| avg_hold_time_bars | 1.6572 |
| exposure | 0.1426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
