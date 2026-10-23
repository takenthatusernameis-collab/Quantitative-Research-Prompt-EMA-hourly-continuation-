# EMA Hourly Continuation — HNT/USDT P12_21

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1502 |
| net_profit_factor | 0.3000 |
| net_win_rate | 0.3768 |
| gross_profit_factor | 0.6653 |
| gross_win_rate | 0.3941 |
| sharpe_ratio | -13.8925 |
| sortino_ratio | -7.6705 |
| max_drawdown | 0.9999 |
| cagr | -0.9798 |
| net_avg_win | 7.5709 |
| net_avg_loss | -15.2613 |
| avg_hold_time_bars | 2.5486 |
| exposure | 0.1740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
