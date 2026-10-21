# EMA Hourly Continuation — DCR/USDT P20_50

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.8829 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -3.3913 |
| sortino_ratio | -1.1678 |
| max_drawdown | 0.7669 |
| cagr | -0.4162 |
| net_avg_win | 43.6469 |
| net_avg_loss | -63.5743 |
| avg_hold_time_bars | 7.7466 |
| exposure | 0.2047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
