# EMA Hourly Continuation — UMA/USDT P34_50

**Symbol:** UMA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.5708 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8643 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -3.6261 |
| sortino_ratio | -0.9872 |
| max_drawdown | 0.6916 |
| cagr | -0.3671 |
| net_avg_win | 55.0386 |
| net_avg_loss | -80.7672 |
| avg_hold_time_bars | 6.2403 |
| exposure | 0.1027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
