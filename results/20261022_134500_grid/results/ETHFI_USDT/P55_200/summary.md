# EMA Hourly Continuation — ETHFI/USDT P55_200

**Symbol:** ETHFI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.8104 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0903 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -1.3916 |
| sortino_ratio | -0.3979 |
| max_drawdown | 0.4216 |
| cagr | -0.1736 |
| net_avg_win | 77.0658 |
| net_avg_loss | -102.9029 |
| avg_hold_time_bars | 19.5911 |
| exposure | 0.3615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
