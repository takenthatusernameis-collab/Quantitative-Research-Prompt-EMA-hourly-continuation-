# EMA Hourly Continuation — ATH/USDT P50_55

**Symbol:** ATH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 107 |
| net_profit_factor | 0.7429 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0100 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -0.9669 |
| sortino_ratio | -0.1484 |
| max_drawdown | 0.1662 |
| cagr | -0.0661 |
| net_avg_win | 79.5228 |
| net_avg_loss | -109.0694 |
| avg_hold_time_bars | 4.3738 |
| exposure | 0.0227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
