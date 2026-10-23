# EMA Hourly Continuation — NOT/USDT P50_100

**Symbol:** NOT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5093 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8045 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -5.0597 |
| sortino_ratio | -1.8305 |
| max_drawdown | 0.8835 |
| cagr | -0.5833 |
| net_avg_win | 31.7480 |
| net_avg_loss | -52.0338 |
| avg_hold_time_bars | 5.6872 |
| exposure | 0.1691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
