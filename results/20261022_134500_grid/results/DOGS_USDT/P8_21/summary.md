# EMA Hourly Continuation — DOGS/USDT P8_21

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1464 |
| net_profit_factor | 0.4268 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.7833 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -10.6223 |
| sortino_ratio | -6.1702 |
| max_drawdown | 0.9987 |
| cagr | -0.9548 |
| net_avg_win | 11.3718 |
| net_avg_loss | -21.5116 |
| avg_hold_time_bars | 2.8777 |
| exposure | 0.2235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
