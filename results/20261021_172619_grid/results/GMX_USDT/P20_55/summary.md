# EMA Hourly Continuation — GMX/USDT P20_55

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.6528 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -3.5715 |
| sortino_ratio | -1.2657 |
| max_drawdown | 0.7767 |
| cagr | -0.4406 |
| net_avg_win | 50.2723 |
| net_avg_loss | -66.7764 |
| avg_hold_time_bars | 8.0356 |
| exposure | 0.2257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
