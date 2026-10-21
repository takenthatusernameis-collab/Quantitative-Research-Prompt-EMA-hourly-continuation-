# EMA Hourly Continuation — DYDX/USDT P12_34

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.7721 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 1.0185 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -2.3411 |
| sortino_ratio | -0.8094 |
| max_drawdown | 0.6457 |
| cagr | -0.3092 |
| net_avg_win | 71.4286 |
| net_avg_loss | -89.6975 |
| avg_hold_time_bars | 7.3636 |
| exposure | 0.1951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
