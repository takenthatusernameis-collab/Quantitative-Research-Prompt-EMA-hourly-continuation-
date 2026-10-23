# EMA Hourly Continuation — ATH/USDT P89_100

**Symbol:** ATH/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.3479 |
| net_win_rate | 0.4269 |
| gross_profit_factor | 0.8117 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -8.0899 |
| sortino_ratio | -2.9294 |
| max_drawdown | 0.9722 |
| cagr | -0.7786 |
| net_avg_win | 20.1638 |
| net_avg_loss | -43.1745 |
| avg_hold_time_bars | 2.0532 |
| exposure | 0.0599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
