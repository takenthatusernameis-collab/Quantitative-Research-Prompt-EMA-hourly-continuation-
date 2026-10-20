# EMA Hourly Continuation — DGB/USDT P20_89

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 834 |
| net_profit_factor | 0.6068 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -5.7937 |
| sortino_ratio | -2.3346 |
| max_drawdown | 0.9469 |
| cagr | -0.6836 |
| net_avg_win | 38.6571 |
| net_avg_loss | -52.5552 |
| avg_hold_time_bars | 9.8681 |
| exposure | 0.3741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
