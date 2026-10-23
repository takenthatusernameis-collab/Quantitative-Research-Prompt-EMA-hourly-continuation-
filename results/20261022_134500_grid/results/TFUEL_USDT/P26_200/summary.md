# EMA Hourly Continuation — TFUEL/USDT P26_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.4984 |
| net_win_rate | 0.3896 |
| gross_profit_factor | 0.7461 |
| gross_win_rate | 0.4039 |
| sharpe_ratio | -5.9787 |
| sortino_ratio | -1.9645 |
| max_drawdown | 0.9153 |
| cagr | -0.6192 |
| net_avg_win | 41.7801 |
| net_avg_loss | -53.5028 |
| avg_hold_time_bars | 20.1293 |
| exposure | 0.5074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
