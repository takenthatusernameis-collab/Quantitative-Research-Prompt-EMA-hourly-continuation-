# EMA Hourly Continuation — ZRX/USDT P55_144

**Symbol:** ZRX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.5883 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9360 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -3.8408 |
| sortino_ratio | -1.2552 |
| max_drawdown | 0.7829 |
| cagr | -0.4540 |
| net_avg_win | 43.2745 |
| net_avg_loss | -67.0579 |
| avg_hold_time_bars | 9.6007 |
| exposure | 0.2361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
