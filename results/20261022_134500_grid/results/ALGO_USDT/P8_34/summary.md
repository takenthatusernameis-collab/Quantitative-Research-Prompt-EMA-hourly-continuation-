# EMA Hourly Continuation — ALGO/USDT P8_34

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1375 |
| net_profit_factor | 0.4778 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9348 |
| gross_win_rate | 0.5004 |
| sharpe_ratio | -7.2449 |
| sortino_ratio | -3.7684 |
| max_drawdown | 0.9910 |
| cagr | -0.8436 |
| net_avg_win | 13.6292 |
| net_avg_loss | -26.7165 |
| avg_hold_time_bars | 5.1898 |
| exposure | 0.3244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
