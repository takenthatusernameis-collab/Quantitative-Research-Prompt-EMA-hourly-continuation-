# EMA Hourly Continuation — PEOPLE/USDT P144_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.5756 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -3.6175 |
| sortino_ratio | -1.0139 |
| max_drawdown | 0.7173 |
| cagr | -0.3852 |
| net_avg_win | 52.1042 |
| net_avg_loss | -78.9352 |
| avg_hold_time_bars | 4.5241 |
| exposure | 0.0809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
