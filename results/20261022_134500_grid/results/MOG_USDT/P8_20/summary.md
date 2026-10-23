# EMA Hourly Continuation — MOG/USDT P8_20

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1525 |
| net_profit_factor | 0.5813 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8682 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -9.2524 |
| sortino_ratio | -5.3006 |
| max_drawdown | 0.9975 |
| cagr | -0.9261 |
| net_avg_win | 20.2153 |
| net_avg_loss | -28.3598 |
| avg_hold_time_bars | 2.9731 |
| exposure | 0.2254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
