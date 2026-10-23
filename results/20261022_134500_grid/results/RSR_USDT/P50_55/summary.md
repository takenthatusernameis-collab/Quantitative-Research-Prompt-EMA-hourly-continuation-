# EMA Hourly Continuation — RSR/USDT P50_55

**Symbol:** RSR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 823 |
| net_profit_factor | 0.2741 |
| net_win_rate | 0.3584 |
| gross_profit_factor | 0.7086 |
| gross_win_rate | 0.3961 |
| sharpe_ratio | -11.9614 |
| sortino_ratio | -5.0045 |
| max_drawdown | 0.9988 |
| cagr | -0.9324 |
| net_avg_win | 12.7830 |
| net_avg_loss | -26.0596 |
| avg_hold_time_bars | 1.8906 |
| exposure | 0.0707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
