# EMA Hourly Continuation — NYM/USDT P50_100

**Symbol:** NYM/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.3919 |
| net_win_rate | 0.4015 |
| gross_profit_factor | 0.6520 |
| gross_win_rate | 0.4052 |
| sharpe_ratio | -4.2010 |
| sortino_ratio | -0.9810 |
| max_drawdown | 0.7000 |
| cagr | -0.3702 |
| net_avg_win | 40.9784 |
| net_avg_loss | -70.1505 |
| avg_hold_time_bars | 12.1301 |
| exposure | 0.1483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
