# EMA Hourly Continuation — BLUR/USDT P12_144

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 1.0281 |
| net_win_rate | 0.5529 |
| gross_profit_factor | 1.2205 |
| gross_win_rate | 0.5529 |
| sharpe_ratio | 0.2111 |
| sortino_ratio | 0.0556 |
| max_drawdown | 0.2035 |
| cagr | 0.0178 |
| net_avg_win | 91.0072 |
| net_avg_loss | -109.4548 |
| avg_hold_time_bars | 48.1571 |
| exposure | 0.7213 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
