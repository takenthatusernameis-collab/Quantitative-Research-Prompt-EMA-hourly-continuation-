# EMA Hourly Continuation — ATOM/USDT P55_200

**Symbol:** ATOM/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7073 |
| net_win_rate | 0.5155 |
| gross_profit_factor | 1.0273 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -1.8831 |
| sortino_ratio | -0.5022 |
| max_drawdown | 0.4677 |
| cagr | -0.2137 |
| net_avg_win | 59.8433 |
| net_avg_loss | -90.0243 |
| avg_hold_time_bars | 20.9859 |
| exposure | 0.3386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
