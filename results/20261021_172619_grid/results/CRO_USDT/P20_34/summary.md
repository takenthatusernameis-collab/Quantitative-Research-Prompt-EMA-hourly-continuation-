# EMA Hourly Continuation — CRO/USDT P20_34

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.5239 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8517 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -3.7880 |
| sortino_ratio | -1.0172 |
| max_drawdown | 0.7003 |
| cagr | -0.3748 |
| net_avg_win | 47.6331 |
| net_avg_loss | -76.9657 |
| avg_hold_time_bars | 5.3897 |
| exposure | 0.0855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
