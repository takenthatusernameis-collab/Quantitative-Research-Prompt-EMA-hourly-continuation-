# EMA Hourly Continuation — ATH/USDT P20_50

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 918 |
| net_profit_factor | 0.5580 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9370 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -5.7324 |
| sortino_ratio | -2.5363 |
| max_drawdown | 0.9460 |
| cagr | -0.7046 |
| net_avg_win | 27.1328 |
| net_avg_loss | -44.5618 |
| avg_hold_time_bars | 4.7658 |
| exposure | 0.2121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
