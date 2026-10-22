# EMA Hourly Continuation — RAY/USDT P20_200

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.6950 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9272 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -2.1082 |
| sortino_ratio | -0.5731 |
| max_drawdown | 0.5237 |
| cagr | -0.2332 |
| net_avg_win | 62.6566 |
| net_avg_loss | -84.4280 |
| avg_hold_time_bars | 37.9754 |
| exposure | 0.6318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
