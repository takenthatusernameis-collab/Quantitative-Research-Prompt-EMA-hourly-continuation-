# EMA Hourly Continuation — GALA/USDT P12_26

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1406 |
| net_profit_factor | 0.3825 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.7740 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -11.0106 |
| sortino_ratio | -5.8628 |
| max_drawdown | 0.9994 |
| cagr | -0.9458 |
| net_avg_win | 10.5456 |
| net_avg_loss | -19.7602 |
| avg_hold_time_bars | 2.7482 |
| exposure | 0.1756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
