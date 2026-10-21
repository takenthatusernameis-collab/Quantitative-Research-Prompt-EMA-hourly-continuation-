# EMA Hourly Continuation — ENS/USDT P8_21

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.7170 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 0.9931 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -2.5963 |
| sortino_ratio | -0.8906 |
| max_drawdown | 0.6418 |
| cagr | -0.3343 |
| net_avg_win | 56.8955 |
| net_avg_loss | -79.0783 |
| avg_hold_time_bars | 6.0525 |
| exposure | 0.1571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
