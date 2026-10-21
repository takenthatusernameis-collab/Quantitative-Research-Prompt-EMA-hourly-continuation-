# EMA Hourly Continuation — WLD/USDT P50_89

**Symbol:** WLD/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8296 |
| net_win_rate | 0.5098 |
| gross_profit_factor | 1.0281 |
| gross_win_rate | 0.5098 |
| sharpe_ratio | -0.9653 |
| sortino_ratio | -0.2426 |
| max_drawdown | 0.2600 |
| cagr | -0.1067 |
| net_avg_win | 77.0387 |
| net_avg_loss | -96.5719 |
| avg_hold_time_bars | 8.0556 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
