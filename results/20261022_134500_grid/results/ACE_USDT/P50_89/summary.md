# EMA Hourly Continuation — ACE/USDT P50_89

**Symbol:** ACE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.6127 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 1.0770 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -3.4178 |
| sortino_ratio | -1.1199 |
| max_drawdown | 0.7402 |
| cagr | -0.4117 |
| net_avg_win | 43.8639 |
| net_avg_loss | -69.7602 |
| avg_hold_time_bars | 6.5881 |
| exposure | 0.1607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
