# EMA Hourly Continuation — JST/USDT P8_12

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.3968 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 1.0294 |
| gross_win_rate | 0.5211 |
| sharpe_ratio | -4.6972 |
| sortino_ratio | -1.3186 |
| max_drawdown | 0.8020 |
| cagr | -0.4673 |
| net_avg_win | 27.6995 |
| net_avg_loss | -69.0754 |
| avg_hold_time_bars | 4.9105 |
| exposure | 0.0844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
