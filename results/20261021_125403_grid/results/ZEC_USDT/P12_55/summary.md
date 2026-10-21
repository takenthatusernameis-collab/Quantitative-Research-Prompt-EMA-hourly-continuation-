# EMA Hourly Continuation — ZEC/USDT P12_55

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.8577 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0456 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -1.1048 |
| sortino_ratio | -0.3730 |
| max_drawdown | 0.3755 |
| cagr | -0.1610 |
| net_avg_win | 75.9408 |
| net_avg_loss | -92.8045 |
| avg_hold_time_bars | 13.0253 |
| exposure | 0.3274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
