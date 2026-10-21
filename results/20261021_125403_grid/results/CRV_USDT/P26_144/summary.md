# EMA Hourly Continuation — CRV/USDT P26_144

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.8865 |
| net_win_rate | 0.5171 |
| gross_profit_factor | 1.0768 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -0.7994 |
| sortino_ratio | -0.2243 |
| max_drawdown | 0.3626 |
| cagr | -0.1009 |
| net_avg_win | 92.9561 |
| net_avg_loss | -112.2621 |
| avg_hold_time_bars | 25.1312 |
| exposure | 0.4352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
