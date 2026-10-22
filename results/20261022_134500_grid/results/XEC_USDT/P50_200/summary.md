# EMA Hourly Continuation — XEC/USDT P50_200

**Symbol:** XEC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.5659 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8683 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -3.6020 |
| sortino_ratio | -1.0191 |
| max_drawdown | 0.7252 |
| cagr | -0.3850 |
| net_avg_win | 49.5283 |
| net_avg_loss | -73.9940 |
| avg_hold_time_bars | 22.9384 |
| exposure | 0.4214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
