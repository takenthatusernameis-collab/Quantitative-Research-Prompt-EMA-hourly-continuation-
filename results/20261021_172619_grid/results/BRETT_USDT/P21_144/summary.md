# EMA Hourly Continuation — BRETT/USDT P21_144

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8579 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -1.6125 |
| sortino_ratio | -0.4215 |
| max_drawdown | 0.3875 |
| cagr | -0.1775 |
| net_avg_win | 78.7702 |
| net_avg_loss | -88.8284 |
| avg_hold_time_bars | 36.3084 |
| exposure | 0.5608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
