# EMA Hourly Continuation — EDU/USDT P20_34

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.5881 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8200 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -3.5457 |
| sortino_ratio | -1.0951 |
| max_drawdown | 0.7226 |
| cagr | -0.3962 |
| net_avg_win | 48.2613 |
| net_avg_loss | -67.7482 |
| avg_hold_time_bars | 5.1401 |
| exposure | 0.1096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
