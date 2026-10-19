# EMA Hourly Continuation — ETHFI/USDT P55_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.7123 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0141 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -2.3916 |
| sortino_ratio | -0.7634 |
| max_drawdown | 0.6091 |
| cagr | -0.3043 |
| net_avg_win | 57.8331 |
| net_avg_loss | -82.1555 |
| avg_hold_time_bars | 10.9646 |
| exposure | 0.2537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
