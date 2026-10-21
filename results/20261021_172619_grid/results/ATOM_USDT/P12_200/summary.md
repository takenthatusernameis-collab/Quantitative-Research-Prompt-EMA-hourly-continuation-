# EMA Hourly Continuation — ATOM/USDT P12_200

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.9147 |
| net_win_rate | 0.5302 |
| gross_profit_factor | 1.1186 |
| gross_win_rate | 0.5302 |
| sharpe_ratio | -0.4496 |
| sortino_ratio | -0.1152 |
| max_drawdown | 0.1727 |
| cagr | -0.0550 |
| net_avg_win | 84.9464 |
| net_avg_loss | -104.7958 |
| avg_hold_time_bars | 49.8921 |
| exposure | 0.7144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
