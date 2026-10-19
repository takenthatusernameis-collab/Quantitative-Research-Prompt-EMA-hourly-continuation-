# EMA Hourly Continuation — LTC/USDT P26_89

**Symbol:** LTC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.4428 |
| net_win_rate | 0.4235 |
| gross_profit_factor | 0.8725 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -7.3181 |
| sortino_ratio | -2.8171 |
| max_drawdown | 0.9703 |
| cagr | -0.7483 |
| net_avg_win | 24.5932 |
| net_avg_loss | -40.8093 |
| avg_hold_time_bars | 8.7524 |
| exposure | 0.2940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
