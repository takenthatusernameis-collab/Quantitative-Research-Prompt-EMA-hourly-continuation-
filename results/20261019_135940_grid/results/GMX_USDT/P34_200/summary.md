# EMA Hourly Continuation — GMX/USDT P34_200

**Symbol:** GMX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6805 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9377 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.8549 |
| sortino_ratio | -0.8519 |
| max_drawdown | 0.6761 |
| cagr | -0.3317 |
| net_avg_win | 63.9478 |
| net_avg_loss | -84.0592 |
| avg_hold_time_bars | 21.7216 |
| exposure | 0.4433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
