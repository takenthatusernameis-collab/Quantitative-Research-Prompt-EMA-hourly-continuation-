# EMA Hourly Continuation — ZEC/USDT P34_100

**Symbol:** ZEC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.6199 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9891 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -3.8468 |
| sortino_ratio | -1.3620 |
| max_drawdown | 0.8105 |
| cagr | -0.4763 |
| net_avg_win | 43.6409 |
| net_avg_loss | -64.5920 |
| avg_hold_time_bars | 8.1467 |
| exposure | 0.2322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
