# EMA Hourly Continuation — RIO/USDT P20_26

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1311 |
| net_profit_factor | 0.2733 |
| net_win_rate | 0.3318 |
| gross_profit_factor | 0.5848 |
| gross_win_rate | 0.3471 |
| sharpe_ratio | -14.3917 |
| sortino_ratio | -7.4802 |
| max_drawdown | 0.9999 |
| cagr | -0.9795 |
| net_avg_win | 8.6463 |
| net_avg_loss | -15.7083 |
| avg_hold_time_bars | 2.1709 |
| exposure | 0.1307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
