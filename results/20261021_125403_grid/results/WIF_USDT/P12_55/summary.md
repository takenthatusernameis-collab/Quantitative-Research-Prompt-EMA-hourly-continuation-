# EMA Hourly Continuation — WIF/USDT P12_55

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.9473 |
| net_win_rate | 0.5310 |
| gross_profit_factor | 1.1319 |
| gross_win_rate | 0.5310 |
| sharpe_ratio | -0.4489 |
| sortino_ratio | -0.1540 |
| max_drawdown | 0.4728 |
| cagr | -0.0758 |
| net_avg_win | 107.5739 |
| net_avg_loss | -128.5567 |
| avg_hold_time_bars | 12.5310 |
| exposure | 0.3218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
