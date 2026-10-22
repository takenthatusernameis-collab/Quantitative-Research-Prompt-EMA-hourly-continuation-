# EMA Hourly Continuation — CRV/USDT P21_100

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.6450 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9801 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -4.0257 |
| sortino_ratio | -1.4992 |
| max_drawdown | 0.8478 |
| cagr | -0.5114 |
| net_avg_win | 45.3874 |
| net_avg_loss | -64.5712 |
| avg_hold_time_bars | 11.4198 |
| exposure | 0.3623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
