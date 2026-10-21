# EMA Hourly Continuation — GRT/USDT P20_89

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7517 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9366 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.0887 |
| sortino_ratio | -0.6610 |
| max_drawdown | 0.5489 |
| cagr | -0.2623 |
| net_avg_win | 67.8871 |
| net_avg_loss | -84.3113 |
| avg_hold_time_bars | 15.2182 |
| exposure | 0.3409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
