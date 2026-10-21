# EMA Hourly Continuation — TAO/USDT P21_55

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7890 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9740 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -1.7388 |
| sortino_ratio | -0.5384 |
| max_drawdown | 0.5015 |
| cagr | -0.2203 |
| net_avg_win | 75.5384 |
| net_avg_loss | -92.1398 |
| avg_hold_time_bars | 8.2516 |
| exposure | 0.1759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
