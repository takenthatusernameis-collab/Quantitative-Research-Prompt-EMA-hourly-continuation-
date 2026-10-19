# EMA Hourly Continuation — JTO/USDT P8_26

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1537 |
| net_profit_factor | 0.5435 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.9519 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -8.3865 |
| sortino_ratio | -4.6197 |
| max_drawdown | 0.9966 |
| cagr | -0.8941 |
| net_avg_win | 17.1171 |
| net_avg_loss | -25.8609 |
| avg_hold_time_bars | 4.1588 |
| exposure | 0.2905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
