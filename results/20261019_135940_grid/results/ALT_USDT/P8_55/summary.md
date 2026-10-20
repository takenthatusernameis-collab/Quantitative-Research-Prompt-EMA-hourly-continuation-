# EMA Hourly Continuation — ALT/USDT P8_55

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 894 |
| net_profit_factor | 0.6308 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.9215 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -5.2303 |
| sortino_ratio | -2.1932 |
| max_drawdown | 0.9300 |
| cagr | -0.6491 |
| net_avg_win | 39.3401 |
| net_avg_loss | -51.1875 |
| avg_hold_time_bars | 12.3356 |
| exposure | 0.5013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
