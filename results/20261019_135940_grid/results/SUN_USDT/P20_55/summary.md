# EMA Hourly Continuation — SUN/USDT P20_55

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.3317 |
| net_win_rate | 0.3688 |
| gross_profit_factor | 0.8439 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -10.8228 |
| sortino_ratio | -4.4079 |
| max_drawdown | 0.9971 |
| cagr | -0.9018 |
| net_avg_win | 16.6087 |
| net_avg_loss | -29.2562 |
| avg_hold_time_bars | 7.8502 |
| exposure | 0.2870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
