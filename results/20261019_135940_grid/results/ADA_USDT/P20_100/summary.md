# EMA Hourly Continuation — ADA/USDT P20_100

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.5562 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -4.5351 |
| sortino_ratio | -1.6675 |
| max_drawdown | 0.8733 |
| cagr | -0.5532 |
| net_avg_win | 33.8775 |
| net_avg_loss | -53.7153 |
| avg_hold_time_bars | 12.4657 |
| exposure | 0.3881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
