# EMA Hourly Continuation — SUN/USDT P50_100

**Symbol:** SUN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.4175 |
| net_win_rate | 0.3975 |
| gross_profit_factor | 0.7511 |
| gross_win_rate | 0.4175 |
| sharpe_ratio | -6.0511 |
| sortino_ratio | -1.7265 |
| max_drawdown | 0.8812 |
| cagr | -0.5687 |
| net_avg_win | 39.6691 |
| net_avg_loss | -62.6923 |
| avg_hold_time_bars | 10.1100 |
| exposure | 0.1830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
