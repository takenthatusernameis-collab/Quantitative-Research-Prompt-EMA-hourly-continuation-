# EMA Hourly Continuation — WIF/USDT P12_21

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1476 |
| net_profit_factor | 0.5292 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -10.6389 |
| sortino_ratio | -5.7472 |
| max_drawdown | 0.9994 |
| cagr | -0.9465 |
| net_avg_win | 17.1225 |
| net_avg_loss | -25.8853 |
| avg_hold_time_bars | 2.1003 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
