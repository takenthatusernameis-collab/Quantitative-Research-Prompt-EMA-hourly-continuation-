# EMA Hourly Continuation — DGB/USDT P21_55

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.4493 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.8410 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -8.5115 |
| sortino_ratio | -3.8983 |
| max_drawdown | 0.9929 |
| cagr | -0.8597 |
| net_avg_win | 17.4212 |
| net_avg_loss | -29.9480 |
| avg_hold_time_bars | 4.5689 |
| exposure | 0.2216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
