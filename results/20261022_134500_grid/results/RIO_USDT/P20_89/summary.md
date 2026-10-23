# EMA Hourly Continuation — RIO/USDT P20_89

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.5858 |
| net_win_rate | 0.4325 |
| gross_profit_factor | 0.8005 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -5.5591 |
| sortino_ratio | -2.3230 |
| max_drawdown | 0.9407 |
| cagr | -0.6733 |
| net_avg_win | 34.8245 |
| net_avg_loss | -45.2971 |
| avg_hold_time_bars | 9.1407 |
| exposure | 0.3697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
