# EMA Hourly Continuation — RPL/USDT P34_55

**Symbol:** RPL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 839 |
| net_profit_factor | 0.4868 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.9337 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -6.4419 |
| sortino_ratio | -2.6478 |
| max_drawdown | 0.9583 |
| cagr | -0.7146 |
| net_avg_win | 23.8420 |
| net_avg_loss | -40.7441 |
| avg_hold_time_bars | 4.5197 |
| exposure | 0.1716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
