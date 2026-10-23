# EMA Hourly Continuation — DIA/USDT P20_200

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7600 |
| net_win_rate | 0.5211 |
| gross_profit_factor | 1.0615 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -1.5309 |
| sortino_ratio | -0.4357 |
| max_drawdown | 0.5287 |
| cagr | -0.1864 |
| net_avg_win | 61.2028 |
| net_avg_loss | -87.6176 |
| avg_hold_time_bars | 34.9454 |
| exposure | 0.6373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
