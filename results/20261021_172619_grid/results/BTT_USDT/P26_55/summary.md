# EMA Hourly Continuation — BTT/USDT P26_55

**Symbol:** BTT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.4415 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.7631 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -5.8867 |
| sortino_ratio | -1.7232 |
| max_drawdown | 0.8712 |
| cagr | -0.5564 |
| net_avg_win | 40.9364 |
| net_avg_loss | -64.9121 |
| avg_hold_time_bars | 9.0907 |
| exposure | 0.1686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
