# EMA Hourly Continuation — DOGS/USDT P8_20

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1482 |
| net_profit_factor | 0.4418 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8152 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -10.8254 |
| sortino_ratio | -6.3286 |
| max_drawdown | 0.9990 |
| cagr | -0.9587 |
| net_avg_win | 11.9442 |
| net_avg_loss | -21.8251 |
| avg_hold_time_bars | 2.7328 |
| exposure | 0.2149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
