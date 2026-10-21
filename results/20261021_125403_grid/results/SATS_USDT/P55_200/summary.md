# EMA Hourly Continuation — SATS/USDT P55_200

**Symbol:** SATS/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.7045 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8589 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -1.7908 |
| sortino_ratio | -0.4280 |
| max_drawdown | 0.4076 |
| cagr | -0.1785 |
| net_avg_win | 70.6179 |
| net_avg_loss | -87.0467 |
| avg_hold_time_bars | 26.7782 |
| exposure | 0.3441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
