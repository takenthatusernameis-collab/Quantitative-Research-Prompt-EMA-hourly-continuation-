# EMA Hourly Continuation — RIO/USDT P12_55

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.9185 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0587 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -0.6808 |
| sortino_ratio | -0.2395 |
| max_drawdown | 0.3447 |
| cagr | -0.1108 |
| net_avg_win | 93.5742 |
| net_avg_loss | -107.5200 |
| avg_hold_time_bars | 11.4512 |
| exposure | 0.3123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
