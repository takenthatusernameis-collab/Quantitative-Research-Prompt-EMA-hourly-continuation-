# EMA Hourly Continuation — DCR/USDT P34_200

**Symbol:** DCR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.6628 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9509 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -2.9622 |
| sortino_ratio | -0.8989 |
| max_drawdown | 0.6893 |
| cagr | -0.3426 |
| net_avg_win | 59.3983 |
| net_avg_loss | -78.6938 |
| avg_hold_time_bars | 21.2727 |
| exposure | 0.4447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
