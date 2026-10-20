# EMA Hourly Continuation — NOT/USDT P34_200

**Symbol:** NOT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.5754 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.7770 |
| gross_win_rate | 0.4370 |
| sharpe_ratio | -3.3568 |
| sortino_ratio | -0.9044 |
| max_drawdown | 0.6654 |
| cagr | -0.3501 |
| net_avg_win | 56.7490 |
| net_avg_loss | -75.6745 |
| avg_hold_time_bars | 32.5686 |
| exposure | 0.5462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
