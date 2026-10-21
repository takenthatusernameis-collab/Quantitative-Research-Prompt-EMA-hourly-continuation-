# EMA Hourly Continuation — WIF/USDT P8_50

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.9714 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1571 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -0.2062 |
| sortino_ratio | -0.0761 |
| max_drawdown | 0.3963 |
| cagr | -0.0451 |
| net_avg_win | 106.3782 |
| net_avg_loss | -127.7555 |
| avg_hold_time_bars | 13.5292 |
| exposure | 0.3997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
