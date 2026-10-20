# EMA Hourly Continuation — XPR/USDT P100_200

**Symbol:** XPR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.4519 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -4.3044 |
| sortino_ratio | -1.1868 |
| max_drawdown | 0.8011 |
| cagr | -0.4509 |
| net_avg_win | 35.6412 |
| net_avg_loss | -67.5994 |
| avg_hold_time_bars | 9.1872 |
| exposure | 0.1629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
