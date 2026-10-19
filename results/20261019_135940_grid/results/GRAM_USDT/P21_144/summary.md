# EMA Hourly Continuation — GRAM/USDT P21_144

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.3908 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.7484 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -5.9135 |
| sortino_ratio | -2.0152 |
| max_drawdown | 0.9237 |
| cagr | -0.6312 |
| net_avg_win | 23.0073 |
| net_avg_loss | -45.1286 |
| avg_hold_time_bars | 18.1085 |
| exposure | 0.4856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
