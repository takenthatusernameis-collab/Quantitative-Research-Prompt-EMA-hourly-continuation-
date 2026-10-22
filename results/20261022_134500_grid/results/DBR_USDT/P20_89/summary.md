# EMA Hourly Continuation — DBR/USDT P20_89

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.4608 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.7571 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -5.6880 |
| sortino_ratio | -2.0170 |
| max_drawdown | 0.8657 |
| cagr | -0.6281 |
| net_avg_win | 33.0580 |
| net_avg_loss | -55.1694 |
| avg_hold_time_bars | 13.5380 |
| exposure | 0.3949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
