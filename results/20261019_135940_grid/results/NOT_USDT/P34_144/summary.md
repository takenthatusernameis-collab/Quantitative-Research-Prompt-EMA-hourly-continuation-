# EMA Hourly Continuation — NOT/USDT P34_144

**Symbol:** NOT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6321 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8917 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -3.5665 |
| sortino_ratio | -1.1036 |
| max_drawdown | 0.7297 |
| cagr | -0.4067 |
| net_avg_win | 57.7037 |
| net_avg_loss | -77.5244 |
| avg_hold_time_bars | 19.9850 |
| exposure | 0.4375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
