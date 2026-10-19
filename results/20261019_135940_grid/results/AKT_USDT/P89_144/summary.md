# EMA Hourly Continuation — AKT/USDT P89_144

**Symbol:** AKT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6266 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 1.0437 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -3.4870 |
| sortino_ratio | -1.1013 |
| max_drawdown | 0.7575 |
| cagr | -0.4084 |
| net_avg_win | 50.5693 |
| net_avg_loss | -77.2139 |
| avg_hold_time_bars | 4.8531 |
| exposure | 0.1096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
