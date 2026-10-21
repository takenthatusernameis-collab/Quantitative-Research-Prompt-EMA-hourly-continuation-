# EMA Hourly Continuation — UNI/USDT P8_55

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.7680 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9514 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -2.2286 |
| sortino_ratio | -0.7990 |
| max_drawdown | 0.6148 |
| cagr | -0.3075 |
| net_avg_win | 65.3918 |
| net_avg_loss | -79.6625 |
| avg_hold_time_bars | 14.8748 |
| exposure | 0.4266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
