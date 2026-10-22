# EMA Hourly Continuation — ADA/USDT P12_200

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.5759 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.9369 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -3.5083 |
| sortino_ratio | -0.9502 |
| max_drawdown | 0.7078 |
| cagr | -0.3790 |
| net_avg_win | 53.5298 |
| net_avg_loss | -79.8637 |
| avg_hold_time_bars | 41.1593 |
| exposure | 0.7165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
