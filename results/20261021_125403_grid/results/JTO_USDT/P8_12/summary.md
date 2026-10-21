# EMA Hourly Continuation — JTO/USDT P8_12

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7558 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0479 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.6075 |
| sortino_ratio | -0.4244 |
| max_drawdown | 0.3853 |
| cagr | -0.1761 |
| net_avg_win | 69.3475 |
| net_avg_loss | -95.6401 |
| avg_hold_time_bars | 4.1840 |
| exposure | 0.0641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
