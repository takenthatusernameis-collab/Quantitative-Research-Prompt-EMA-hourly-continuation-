# EMA Hourly Continuation — GRT/USDT P26_50

**Symbol:** GRT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 949 |
| net_profit_factor | 0.4172 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.7564 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -8.1331 |
| sortino_ratio | -3.5380 |
| max_drawdown | 0.9882 |
| cagr | -0.8255 |
| net_avg_win | 17.4162 |
| net_avg_loss | -31.2129 |
| avg_hold_time_bars | 3.5395 |
| exposure | 0.1520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
