# EMA Hourly Continuation — RAY/USDT P12_21

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7010 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9772 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -2.0967 |
| sortino_ratio | -0.5717 |
| max_drawdown | 0.5532 |
| cagr | -0.2315 |
| net_avg_win | 63.0057 |
| net_avg_loss | -88.8956 |
| avg_hold_time_bars | 4.7569 |
| exposure | 0.0783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
