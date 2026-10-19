# EMA Hourly Continuation — JASMY/USDT P8_55

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1157 |
| net_profit_factor | 0.5746 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -6.1683 |
| sortino_ratio | -2.9204 |
| max_drawdown | 0.9751 |
| cagr | -0.7637 |
| net_avg_win | 24.2063 |
| net_avg_loss | -37.2590 |
| avg_hold_time_bars | 8.3397 |
| exposure | 0.4386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
