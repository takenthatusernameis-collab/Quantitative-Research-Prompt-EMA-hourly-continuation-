# EMA Hourly Continuation — FIDA/USDT P21_89

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6815 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.8792 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.4422 |
| sortino_ratio | -0.7842 |
| max_drawdown | 0.6244 |
| cagr | -0.3028 |
| net_avg_win | 52.3880 |
| net_avg_loss | -70.5153 |
| avg_hold_time_bars | 16.4294 |
| exposure | 0.3792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
