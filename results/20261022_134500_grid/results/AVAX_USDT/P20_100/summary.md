# EMA Hourly Continuation — AVAX/USDT P20_100

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.7173 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.1134 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -3.5995 |
| sortino_ratio | -1.2848 |
| max_drawdown | 0.8192 |
| cagr | -0.4662 |
| net_avg_win | 61.5696 |
| net_avg_loss | -85.8296 |
| avg_hold_time_bars | 13.0581 |
| exposure | 0.3882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
