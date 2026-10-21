# EMA Hourly Continuation — ERG/USDT P8_21

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.5609 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.7951 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -4.1171 |
| sortino_ratio | -1.2819 |
| max_drawdown | 0.7770 |
| cagr | -0.4486 |
| net_avg_win | 47.1848 |
| net_avg_loss | -65.4292 |
| avg_hold_time_bars | 6.3917 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
