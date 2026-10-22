# EMA Hourly Continuation — MLK/USDT P26_200

**Symbol:** MLK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.5295 |
| net_win_rate | 0.3820 |
| gross_profit_factor | 0.6674 |
| gross_win_rate | 0.3820 |
| sharpe_ratio | -4.3120 |
| sortino_ratio | -1.1727 |
| max_drawdown | 0.7566 |
| cagr | -0.4238 |
| net_avg_win | 58.7076 |
| net_avg_loss | -68.5175 |
| avg_hold_time_bars | 28.4191 |
| exposure | 0.4849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
