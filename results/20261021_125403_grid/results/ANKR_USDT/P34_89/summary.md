# EMA Hourly Continuation — ANKR/USDT P34_89

**Symbol:** ANKR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6223 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8445 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -3.8645 |
| sortino_ratio | -1.2180 |
| max_drawdown | 0.7589 |
| cagr | -0.4303 |
| net_avg_win | 57.4390 |
| net_avg_loss | -73.3714 |
| avg_hold_time_bars | 11.8898 |
| exposure | 0.2648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
