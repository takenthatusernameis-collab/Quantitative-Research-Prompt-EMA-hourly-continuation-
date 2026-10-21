# EMA Hourly Continuation — XMR/USDT P34_144

**Symbol:** XMR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6196 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8165 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -3.1939 |
| sortino_ratio | -0.9544 |
| max_drawdown | 0.6801 |
| cagr | -0.3551 |
| net_avg_win | 55.1992 |
| net_avg_loss | -71.6342 |
| avg_hold_time_bars | 15.8190 |
| exposure | 0.3178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
