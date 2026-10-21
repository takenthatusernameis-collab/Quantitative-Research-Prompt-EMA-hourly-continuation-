# EMA Hourly Continuation — AKT/USDT P8_100

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.8202 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9617 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -1.4014 |
| sortino_ratio | -0.4409 |
| max_drawdown | 0.4197 |
| cagr | -0.1861 |
| net_avg_win | 77.4137 |
| net_avg_loss | -90.5727 |
| avg_hold_time_bars | 27.7428 |
| exposure | 0.6129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
