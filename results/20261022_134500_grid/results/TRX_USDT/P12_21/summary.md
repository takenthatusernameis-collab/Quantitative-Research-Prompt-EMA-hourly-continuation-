# EMA Hourly Continuation — TRX/USDT P12_21

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1248 |
| net_profit_factor | 0.0674 |
| net_win_rate | 0.2123 |
| gross_profit_factor | 0.7554 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -21.5782 |
| sortino_ratio | -12.8679 |
| max_drawdown | 1.0000 |
| cagr | -0.9992 |
| net_avg_win | 2.7293 |
| net_avg_loss | -10.9087 |
| avg_hold_time_bars | 2.7356 |
| exposure | 0.1552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
