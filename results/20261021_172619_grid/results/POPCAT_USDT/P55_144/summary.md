# EMA Hourly Continuation — POPCAT/USDT P55_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7338 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8739 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -1.8355 |
| sortino_ratio | -0.4949 |
| max_drawdown | 0.4105 |
| cagr | -0.2042 |
| net_avg_win | 74.0533 |
| net_avg_loss | -88.6889 |
| avg_hold_time_bars | 17.2000 |
| exposure | 0.2817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
