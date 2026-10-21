# EMA Hourly Continuation — GMX/USDT P21_50

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.6805 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -3.1828 |
| sortino_ratio | -1.1147 |
| max_drawdown | 0.7360 |
| cagr | -0.3997 |
| net_avg_win | 53.2429 |
| net_avg_loss | -72.7060 |
| avg_hold_time_bars | 7.3450 |
| exposure | 0.2003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
