# EMA Hourly Continuation — LTC/USDT P8_144

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.4127 |
| net_win_rate | 0.4192 |
| gross_profit_factor | 0.7730 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -6.2975 |
| sortino_ratio | -2.1305 |
| max_drawdown | 0.9386 |
| cagr | -0.6638 |
| net_avg_win | 26.3963 |
| net_avg_loss | -46.1610 |
| avg_hold_time_bars | 26.0269 |
| exposure | 0.7027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
