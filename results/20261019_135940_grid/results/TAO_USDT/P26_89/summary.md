# EMA Hourly Continuation — TAO/USDT P26_89

**Symbol:** TAO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.6833 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -3.5236 |
| sortino_ratio | -1.3192 |
| max_drawdown | 0.8083 |
| cagr | -0.4714 |
| net_avg_win | 48.7873 |
| net_avg_loss | -70.2102 |
| avg_hold_time_bars | 9.1517 |
| exposure | 0.2962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
