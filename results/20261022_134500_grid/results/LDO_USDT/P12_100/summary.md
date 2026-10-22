# EMA Hourly Continuation — LDO/USDT P12_100

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.6161 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8397 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -3.8401 |
| sortino_ratio | -1.3253 |
| max_drawdown | 0.7983 |
| cagr | -0.4674 |
| net_avg_win | 46.6994 |
| net_avg_loss | -63.0912 |
| avg_hold_time_bars | 21.7720 |
| exposure | 0.5948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
