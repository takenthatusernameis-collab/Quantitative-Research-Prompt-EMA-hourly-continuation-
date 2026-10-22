# EMA Hourly Continuation — LTC/USDT P8_26

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1551 |
| net_profit_factor | 0.2589 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.8195 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -12.9765 |
| sortino_ratio | -7.2372 |
| max_drawdown | 0.9999 |
| cagr | -0.9769 |
| net_avg_win | 5.3824 |
| net_avg_loss | -14.9583 |
| avg_hold_time_bars | 3.6312 |
| exposure | 0.2560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
