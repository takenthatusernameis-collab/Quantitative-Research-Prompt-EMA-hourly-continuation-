# EMA Hourly Continuation — CETUS/USDT P8_144

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 1.1078 |
| net_win_rate | 0.5640 |
| gross_profit_factor | 1.2875 |
| gross_win_rate | 0.5640 |
| sharpe_ratio | 0.6304 |
| sortino_ratio | 0.1663 |
| max_drawdown | 0.1600 |
| cagr | 0.0676 |
| net_avg_win | 99.5843 |
| net_avg_loss | -116.2971 |
| avg_hold_time_bars | 52.0305 |
| exposure | 0.7723 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
