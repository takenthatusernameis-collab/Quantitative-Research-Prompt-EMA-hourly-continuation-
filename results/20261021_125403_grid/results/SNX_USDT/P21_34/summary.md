# EMA Hourly Continuation — SNX/USDT P21_34

**Symbol:** SNX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7062 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9914 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.9436 |
| sortino_ratio | -0.4974 |
| max_drawdown | 0.4565 |
| cagr | -0.2036 |
| net_avg_win | 66.0575 |
| net_avg_loss | -92.9522 |
| avg_hold_time_bars | 4.6959 |
| exposure | 0.0678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
