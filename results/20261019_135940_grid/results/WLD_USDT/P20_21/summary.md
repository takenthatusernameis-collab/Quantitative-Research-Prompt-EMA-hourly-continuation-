# EMA Hourly Continuation — WLD/USDT P20_21

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.1830 |
| net_win_rate | 0.3123 |
| gross_profit_factor | 0.5688 |
| gross_win_rate | 0.3560 |
| sharpe_ratio | -16.8392 |
| sortino_ratio | -8.6537 |
| max_drawdown | 1.0000 |
| cagr | -0.9926 |
| net_avg_win | 6.0216 |
| net_avg_loss | -14.9450 |
| avg_hold_time_bars | 1.4668 |
| exposure | 0.0794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
