# EMA Hourly Continuation — DODO/USDT P55_100

**Symbol:** DODO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6693 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -2.7158 |
| sortino_ratio | -0.7819 |
| max_drawdown | 0.6061 |
| cagr | -0.3017 |
| net_avg_win | 62.8038 |
| net_avg_loss | -83.0260 |
| avg_hold_time_bars | 7.4670 |
| exposure | 0.1382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
