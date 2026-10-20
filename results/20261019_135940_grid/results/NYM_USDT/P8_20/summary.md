# EMA Hourly Continuation — NYM/USDT P8_20

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1489 |
| net_profit_factor | 0.1713 |
| net_win_rate | 0.2975 |
| gross_profit_factor | 0.5858 |
| gross_win_rate | 0.3573 |
| sharpe_ratio | -19.4853 |
| sortino_ratio | -11.2216 |
| max_drawdown | 1.0000 |
| cagr | -0.9981 |
| net_avg_win | 4.6651 |
| net_avg_loss | -11.5360 |
| avg_hold_time_bars | 4.7931 |
| exposure | 0.3244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
