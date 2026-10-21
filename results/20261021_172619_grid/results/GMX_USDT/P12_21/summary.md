# EMA Hourly Continuation — GMX/USDT P12_21

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.5942 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9004 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -3.7851 |
| sortino_ratio | -1.2303 |
| max_drawdown | 0.7578 |
| cagr | -0.4314 |
| net_avg_win | 45.8564 |
| net_avg_loss | -68.6590 |
| avg_hold_time_bars | 5.4903 |
| exposure | 0.1283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
