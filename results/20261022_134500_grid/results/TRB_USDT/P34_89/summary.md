# EMA Hourly Continuation — TRB/USDT P34_89

**Symbol:** TRB/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.4941 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -6.2439 |
| sortino_ratio | -2.3487 |
| max_drawdown | 0.9466 |
| cagr | -0.6814 |
| net_avg_win | 29.3703 |
| net_avg_loss | -46.5435 |
| avg_hold_time_bars | 8.0294 |
| exposure | 0.2598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
