# EMA Hourly Continuation — AAVE/USDT P26_55

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.7035 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9365 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.3205 |
| sortino_ratio | -0.6576 |
| max_drawdown | 0.5459 |
| cagr | -0.2598 |
| net_avg_win | 66.9231 |
| net_avg_loss | -87.2405 |
| avg_hold_time_bars | 7.0534 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
