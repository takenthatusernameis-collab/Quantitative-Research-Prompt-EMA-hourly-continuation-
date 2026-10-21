# EMA Hourly Continuation — UNI/USDT P20_21

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 96 |
| net_profit_factor | 0.6350 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8774 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -1.3605 |
| sortino_ratio | -0.1906 |
| max_drawdown | 0.2352 |
| cagr | -0.0835 |
| net_avg_win | 76.0795 |
| net_avg_loss | -105.7098 |
| avg_hold_time_bars | 4.7500 |
| exposure | 0.0207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
