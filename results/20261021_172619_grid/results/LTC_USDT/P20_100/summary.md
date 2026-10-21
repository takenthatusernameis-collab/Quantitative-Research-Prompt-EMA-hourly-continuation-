# EMA Hourly Continuation — LTC/USDT P20_100

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5990 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8107 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -3.3144 |
| sortino_ratio | -0.9862 |
| max_drawdown | 0.6922 |
| cagr | -0.3644 |
| net_avg_win | 51.5405 |
| net_avg_loss | -70.6229 |
| avg_hold_time_bars | 19.7025 |
| exposure | 0.3914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
