# EMA Hourly Continuation — RIO/USDT P20_100

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 851 |
| net_profit_factor | 0.6080 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8094 |
| gross_win_rate | 0.4336 |
| sharpe_ratio | -5.3024 |
| sortino_ratio | -2.1815 |
| max_drawdown | 0.9329 |
| cagr | -0.6477 |
| net_avg_win | 38.9996 |
| net_avg_loss | -48.8704 |
| avg_hold_time_bars | 10.0881 |
| exposure | 0.3941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
