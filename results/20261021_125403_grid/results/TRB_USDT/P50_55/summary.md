# EMA Hourly Continuation — TRB/USDT P50_55

**Symbol:** TRB/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 135 |
| net_profit_factor | 0.6113 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9115 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -1.8330 |
| sortino_ratio | -0.3050 |
| max_drawdown | 0.3157 |
| cagr | -0.1313 |
| net_avg_win | 73.4690 |
| net_avg_loss | -108.3304 |
| avg_hold_time_bars | 4.4296 |
| exposure | 0.0271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
