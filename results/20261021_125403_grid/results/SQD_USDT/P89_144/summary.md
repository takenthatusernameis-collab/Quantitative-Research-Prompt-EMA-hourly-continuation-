# EMA Hourly Continuation — SQD/USDT P89_144

**Symbol:** SQD/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.7908 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9796 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -1.2034 |
| sortino_ratio | -0.2848 |
| max_drawdown | 0.2956 |
| cagr | -0.1235 |
| net_avg_win | 79.0183 |
| net_avg_loss | -97.6879 |
| avg_hold_time_bars | 7.5057 |
| exposure | 0.0935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
