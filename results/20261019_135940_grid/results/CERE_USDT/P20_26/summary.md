# EMA Hourly Continuation — CERE/USDT P20_26

**Symbol:** CERE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1234 |
| net_profit_factor | 0.1786 |
| net_win_rate | 0.2277 |
| gross_profit_factor | 0.6652 |
| gross_win_rate | 0.3169 |
| sharpe_ratio | -19.5316 |
| sortino_ratio | -10.4477 |
| max_drawdown | 1.0000 |
| cagr | -0.9970 |
| net_avg_win | 7.7367 |
| net_avg_loss | -12.7744 |
| avg_hold_time_bars | 3.2034 |
| exposure | 0.1797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
