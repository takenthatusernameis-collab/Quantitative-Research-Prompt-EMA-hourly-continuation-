# EMA Hourly Continuation — WOO/USDT P8_100

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.8080 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9673 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.7090 |
| sortino_ratio | -0.5432 |
| max_drawdown | 0.5206 |
| cagr | -0.2222 |
| net_avg_win | 81.3823 |
| net_avg_loss | -95.5874 |
| avg_hold_time_bars | 29.5976 |
| exposure | 0.6686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
