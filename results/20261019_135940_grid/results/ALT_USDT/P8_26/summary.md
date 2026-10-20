# EMA Hourly Continuation — ALT/USDT P8_26

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1279 |
| net_profit_factor | 0.5487 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.9373 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -7.6454 |
| sortino_ratio | -3.8433 |
| max_drawdown | 0.9911 |
| cagr | -0.8458 |
| net_avg_win | 20.8777 |
| net_avg_loss | -31.2750 |
| avg_hold_time_bars | 5.0985 |
| exposure | 0.2964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
