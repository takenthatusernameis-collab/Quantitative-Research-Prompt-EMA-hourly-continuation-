# EMA Hourly Continuation — AKT/USDT P12_55

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1034 |
| net_profit_factor | 0.5331 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8572 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -6.0179 |
| sortino_ratio | -2.7155 |
| max_drawdown | 0.9658 |
| cagr | -0.7321 |
| net_avg_win | 23.1084 |
| net_avg_loss | -36.9777 |
| avg_hold_time_bars | 7.2456 |
| exposure | 0.3405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
