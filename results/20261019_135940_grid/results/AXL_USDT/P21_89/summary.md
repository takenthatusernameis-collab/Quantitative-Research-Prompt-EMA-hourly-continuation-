# EMA Hourly Continuation — AXL/USDT P21_89

**Symbol:** AXL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 836 |
| net_profit_factor | 0.5994 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.8904 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -5.5621 |
| sortino_ratio | -2.2533 |
| max_drawdown | 0.9373 |
| cagr | -0.6595 |
| net_avg_win | 38.3944 |
| net_avg_loss | -49.3967 |
| avg_hold_time_bars | 9.1962 |
| exposure | 0.3479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
