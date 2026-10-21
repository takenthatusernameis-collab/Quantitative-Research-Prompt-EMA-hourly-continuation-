# EMA Hourly Continuation — KSM/USDT P26_55

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7341 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0307 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -2.0863 |
| sortino_ratio | -0.6533 |
| max_drawdown | 0.5448 |
| cagr | -0.2579 |
| net_avg_win | 60.1444 |
| net_avg_loss | -85.4627 |
| avg_hold_time_bars | 7.4198 |
| exposure | 0.1599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
