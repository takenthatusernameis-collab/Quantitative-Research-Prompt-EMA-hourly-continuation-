# EMA Hourly Continuation — BSV/USDT P20_21

**Symbol:** BSV/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 179 |
| net_profit_factor | 0.6580 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0354 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.7459 |
| sortino_ratio | -0.3367 |
| max_drawdown | 0.3990 |
| cagr | -0.1418 |
| net_avg_win | 67.4438 |
| net_avg_loss | -105.9868 |
| avg_hold_time_bars | 5.6034 |
| exposure | 0.0456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
