# EMA Hourly Continuation — ZKJ/USDT P34_144

**Symbol:** ZKJ/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.2189 |
| net_win_rate | 0.3262 |
| gross_profit_factor | 0.5992 |
| gross_win_rate | 0.3978 |
| sharpe_ratio | -7.0134 |
| sortino_ratio | -1.7212 |
| max_drawdown | 0.8974 |
| cagr | -0.5894 |
| net_avg_win | 27.4984 |
| net_avg_loss | -60.8135 |
| avg_hold_time_bars | 62.6595 |
| exposure | 0.7946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
