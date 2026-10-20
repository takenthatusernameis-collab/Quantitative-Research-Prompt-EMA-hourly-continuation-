# EMA Hourly Continuation — DEGEN/USDT P12_21

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1358 |
| net_profit_factor | 0.4918 |
| net_win_rate | 0.4183 |
| gross_profit_factor | 0.8229 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -10.1134 |
| sortino_ratio | -5.2678 |
| max_drawdown | 0.9986 |
| cagr | -0.9259 |
| net_avg_win | 17.0102 |
| net_avg_loss | -24.8698 |
| avg_hold_time_bars | 2.7099 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
