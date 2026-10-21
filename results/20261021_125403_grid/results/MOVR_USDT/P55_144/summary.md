# EMA Hourly Continuation — MOVR/USDT P55_144

**Symbol:** MOVR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7426 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9300 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -1.6853 |
| sortino_ratio | -0.4668 |
| max_drawdown | 0.4449 |
| cagr | -0.1934 |
| net_avg_win | 65.7533 |
| net_avg_loss | -83.9566 |
| avg_hold_time_bars | 14.3936 |
| exposure | 0.2460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
