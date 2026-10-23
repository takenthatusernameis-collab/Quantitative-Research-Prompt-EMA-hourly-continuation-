# EMA Hourly Continuation — KSM/USDT P34_200

**Symbol:** KSM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6988 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 1.0089 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.2663 |
| sortino_ratio | -0.5951 |
| max_drawdown | 0.5465 |
| cagr | -0.2475 |
| net_avg_win | 68.4360 |
| net_avg_loss | -96.8139 |
| avg_hold_time_bars | 33.5374 |
| exposure | 0.5305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
