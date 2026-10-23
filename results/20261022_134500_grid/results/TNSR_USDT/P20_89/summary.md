# EMA Hourly Continuation — TNSR/USDT P20_89

**Symbol:** TNSR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.7326 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 1.0340 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -3.0377 |
| sortino_ratio | -1.1491 |
| max_drawdown | 0.7724 |
| cagr | -0.4203 |
| net_avg_win | 57.1729 |
| net_avg_loss | -76.9704 |
| avg_hold_time_bars | 11.8211 |
| exposure | 0.3857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
