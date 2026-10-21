# EMA Hourly Continuation — ID/USDT P21_55

**Symbol:** ID/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.6980 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9580 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.8018 |
| sortino_ratio | -0.9669 |
| max_drawdown | 0.6832 |
| cagr | -0.3580 |
| net_avg_win | 54.5732 |
| net_avg_loss | -74.2767 |
| avg_hold_time_bars | 8.4034 |
| exposure | 0.2225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
