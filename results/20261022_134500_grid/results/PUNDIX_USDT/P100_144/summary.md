# EMA Hourly Continuation — PUNDIX/USDT P100_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.4302 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.9071 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -5.4814 |
| sortino_ratio | -1.7521 |
| max_drawdown | 0.8818 |
| cagr | -0.5716 |
| net_avg_win | 28.7987 |
| net_avg_loss | -57.0572 |
| avg_hold_time_bars | 5.4163 |
| exposure | 0.1236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
