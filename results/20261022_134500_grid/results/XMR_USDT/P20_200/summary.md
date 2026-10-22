# EMA Hourly Continuation — XMR/USDT P20_200

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5365 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.9135 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -5.1718 |
| sortino_ratio | -1.8285 |
| max_drawdown | 0.8947 |
| cagr | -0.5896 |
| net_avg_win | 36.1462 |
| net_avg_loss | -55.0568 |
| avg_hold_time_bars | 19.9198 |
| exposure | 0.5759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
