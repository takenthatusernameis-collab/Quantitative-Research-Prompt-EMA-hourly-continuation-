# EMA Hourly Continuation — W/USDT P21_89

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.7453 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0707 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -2.6616 |
| sortino_ratio | -1.0128 |
| max_drawdown | 0.7359 |
| cagr | -0.3787 |
| net_avg_win | 55.7387 |
| net_avg_loss | -77.5455 |
| avg_hold_time_bars | 11.7580 |
| exposure | 0.3843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
