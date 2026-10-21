# EMA Hourly Continuation — CELO/USDT P12_200

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.9071 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0659 |
| gross_win_rate | 0.5182 |
| sharpe_ratio | -0.5213 |
| sortino_ratio | -0.1299 |
| max_drawdown | 0.2603 |
| cagr | -0.0614 |
| net_avg_win | 91.9083 |
| net_avg_loss | -108.9518 |
| avg_hold_time_bars | 54.7459 |
| exposure | 0.7506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
