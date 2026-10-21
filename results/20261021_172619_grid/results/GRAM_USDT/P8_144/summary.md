# EMA Hourly Continuation — GRAM/USDT P8_144

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7893 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0181 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.3853 |
| sortino_ratio | -0.3799 |
| max_drawdown | 0.4091 |
| cagr | -0.1610 |
| net_avg_win | 71.8123 |
| net_avg_loss | -93.4947 |
| avg_hold_time_bars | 43.0790 |
| exposure | 0.7186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
