# EMA Hourly Continuation — SUI/USDT P20_55

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.8229 |
| net_win_rate | 0.5131 |
| gross_profit_factor | 1.0525 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -1.3384 |
| sortino_ratio | -0.4119 |
| max_drawdown | 0.4309 |
| cagr | -0.1732 |
| net_avg_win | 75.0932 |
| net_avg_loss | -96.1592 |
| avg_hold_time_bars | 9.6747 |
| exposure | 0.2014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
