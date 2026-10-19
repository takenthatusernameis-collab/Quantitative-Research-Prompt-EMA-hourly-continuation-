# EMA Hourly Continuation — AKT/USDT P8_100

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.6111 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8795 |
| gross_win_rate | 0.4666 |
| sharpe_ratio | -4.2646 |
| sortino_ratio | -1.6085 |
| max_drawdown | 0.8592 |
| cagr | -0.5353 |
| net_avg_win | 40.5523 |
| net_avg_loss | -56.7539 |
| avg_hold_time_bars | 19.3384 |
| exposure | 0.6311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
