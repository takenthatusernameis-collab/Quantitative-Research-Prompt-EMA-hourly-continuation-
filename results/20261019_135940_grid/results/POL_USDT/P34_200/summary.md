# EMA Hourly Continuation — POL/USDT P34_200

**Symbol:** POL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6464 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9906 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -2.2335 |
| sortino_ratio | -0.6115 |
| max_drawdown | 0.5467 |
| cagr | -0.2546 |
| net_avg_win | 50.7495 |
| net_avg_loss | -76.4789 |
| avg_hold_time_bars | 32.2887 |
| exposure | 0.5592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
