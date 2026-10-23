# EMA Hourly Continuation — OGN/USDT P21_50

**Symbol:** OGN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.4990 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.9110 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -8.0071 |
| sortino_ratio | -3.5234 |
| max_drawdown | 0.9868 |
| cagr | -0.8172 |
| net_avg_win | 23.6084 |
| net_avg_loss | -35.6585 |
| avg_hold_time_bars | 5.1519 |
| exposure | 0.2257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
