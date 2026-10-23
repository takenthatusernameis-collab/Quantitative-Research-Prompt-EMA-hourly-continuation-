# EMA Hourly Continuation — MLK/USDT P8_26

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1827 |
| net_profit_factor | 0.2200 |
| net_win_rate | 0.2671 |
| gross_profit_factor | 0.5978 |
| gross_win_rate | 0.2857 |
| sharpe_ratio | -20.3494 |
| sortino_ratio | -12.5436 |
| max_drawdown | 1.0000 |
| cagr | -0.9985 |
| net_avg_win | 5.7803 |
| net_avg_loss | -9.5749 |
| avg_hold_time_bars | 3.5599 |
| exposure | 0.2943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
