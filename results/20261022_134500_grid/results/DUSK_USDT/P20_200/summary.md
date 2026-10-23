# EMA Hourly Continuation — DUSK/USDT P20_200

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7403 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9715 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -1.7363 |
| sortino_ratio | -0.4669 |
| max_drawdown | 0.4630 |
| cagr | -0.1954 |
| net_avg_win | 69.3336 |
| net_avg_loss | -87.1082 |
| avg_hold_time_bars | 38.4318 |
| exposure | 0.6271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
