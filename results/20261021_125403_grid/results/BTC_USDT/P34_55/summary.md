# EMA Hourly Continuation — BTC/USDT P34_55

**Symbol:** BTC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.4509 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9410 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -4.0183 |
| sortino_ratio | -0.9691 |
| max_drawdown | 0.7240 |
| cagr | -0.3618 |
| net_avg_win | 40.3499 |
| net_avg_loss | -78.7773 |
| avg_hold_time_bars | 6.8248 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
