# EMA Hourly Continuation — FET/USDT P8_50

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1168 |
| net_profit_factor | 0.6124 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9245 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -5.1781 |
| sortino_ratio | -2.4924 |
| max_drawdown | 0.9519 |
| cagr | -0.6961 |
| net_avg_win | 26.6101 |
| net_avg_loss | -40.5723 |
| avg_hold_time_bars | 8.2517 |
| exposure | 0.4381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
