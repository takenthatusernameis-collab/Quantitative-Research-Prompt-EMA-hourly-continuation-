# EMA Hourly Continuation — XNO/USDT P55_89

**Symbol:** XNO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 850 |
| net_profit_factor | 0.3657 |
| net_win_rate | 0.3776 |
| gross_profit_factor | 0.6649 |
| gross_win_rate | 0.3906 |
| sharpe_ratio | -9.5145 |
| sortino_ratio | -3.9650 |
| max_drawdown | 0.9925 |
| cagr | -0.8571 |
| net_avg_win | 17.8220 |
| net_avg_loss | -29.5754 |
| avg_hold_time_bars | 3.6235 |
| exposure | 0.1400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
