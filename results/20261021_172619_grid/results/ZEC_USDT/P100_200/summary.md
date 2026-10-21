# EMA Hourly Continuation — ZEC/USDT P100_200

**Symbol:** ZEC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.8170 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0005 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -0.8655 |
| sortino_ratio | -0.1952 |
| max_drawdown | 0.2549 |
| cagr | -0.0871 |
| net_avg_win | 72.5248 |
| net_avg_loss | -91.6759 |
| avg_hold_time_bars | 14.5403 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
