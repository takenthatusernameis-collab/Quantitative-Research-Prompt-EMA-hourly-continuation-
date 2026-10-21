# EMA Hourly Continuation — SUN/USDT P50_55

**Symbol:** SUN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 0.2777 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.7405 |
| gross_win_rate | 0.3944 |
| sharpe_ratio | -5.9285 |
| sortino_ratio | -1.2814 |
| max_drawdown | 0.8031 |
| cagr | -0.4710 |
| net_avg_win | 43.2970 |
| net_avg_loss | -77.9440 |
| avg_hold_time_bars | 5.5446 |
| exposure | 0.0534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
