# EMA Hourly Continuation — LTC/USDT P26_144

**Symbol:** LTC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.3649 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.7555 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -6.2952 |
| sortino_ratio | -2.0556 |
| max_drawdown | 0.9295 |
| cagr | -0.6445 |
| net_avg_win | 23.6294 |
| net_avg_loss | -45.5371 |
| avg_hold_time_bars | 17.6991 |
| exposure | 0.4385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
