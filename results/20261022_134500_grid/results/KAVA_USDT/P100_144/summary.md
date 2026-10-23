# EMA Hourly Continuation — KAVA/USDT P100_144

**Symbol:** KAVA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.3518 |
| net_win_rate | 0.3923 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -7.4934 |
| sortino_ratio | -2.4449 |
| max_drawdown | 0.9574 |
| cagr | -0.7121 |
| net_avg_win | 25.4380 |
| net_avg_loss | -46.6794 |
| avg_hold_time_bars | 4.6462 |
| exposure | 0.1098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
