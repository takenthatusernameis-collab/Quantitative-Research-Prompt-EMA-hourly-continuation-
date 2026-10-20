# EMA Hourly Continuation — MEW/USDT P26_100

**Symbol:** MEW/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.5650 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8254 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -4.5615 |
| sortino_ratio | -1.6459 |
| max_drawdown | 0.8715 |
| cagr | -0.5492 |
| net_avg_win | 37.1965 |
| net_avg_loss | -54.6182 |
| avg_hold_time_bars | 10.7508 |
| exposure | 0.3255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
