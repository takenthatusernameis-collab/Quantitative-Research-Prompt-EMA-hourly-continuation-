# EMA Hourly Continuation — REQ/USDT P89_200

**Symbol:** REQ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.3754 |
| net_win_rate | 0.3628 |
| gross_profit_factor | 0.7975 |
| gross_win_rate | 0.3881 |
| sharpe_ratio | -8.3368 |
| sortino_ratio | -2.7992 |
| max_drawdown | 0.9719 |
| cagr | -0.7582 |
| net_avg_win | 29.0507 |
| net_avg_loss | -44.0688 |
| avg_hold_time_bars | 8.5397 |
| exposure | 0.2150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
