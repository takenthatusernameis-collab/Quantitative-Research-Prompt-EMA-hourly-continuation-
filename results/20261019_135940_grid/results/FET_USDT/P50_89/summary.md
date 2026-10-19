# EMA Hourly Continuation — FET/USDT P50_89

**Symbol:** FET/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5293 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.8743 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -4.9374 |
| sortino_ratio | -1.7367 |
| max_drawdown | 0.8893 |
| cagr | -0.5749 |
| net_avg_win | 33.4388 |
| net_avg_loss | -55.3514 |
| avg_hold_time_bars | 5.0943 |
| exposure | 0.1473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
