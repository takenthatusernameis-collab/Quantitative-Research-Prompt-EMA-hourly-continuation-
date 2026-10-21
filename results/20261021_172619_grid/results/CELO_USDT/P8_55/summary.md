# EMA Hourly Continuation — CELO/USDT P8_55

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.7764 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -2.2968 |
| sortino_ratio | -0.8773 |
| max_drawdown | 0.6452 |
| cagr | -0.3325 |
| net_avg_win | 62.8672 |
| net_avg_loss | -78.5288 |
| avg_hold_time_bars | 14.9135 |
| exposure | 0.4839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
