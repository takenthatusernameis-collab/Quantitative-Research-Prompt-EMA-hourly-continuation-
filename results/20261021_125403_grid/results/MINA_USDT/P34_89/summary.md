# EMA Hourly Continuation — MINA/USDT P34_89

**Symbol:** MINA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.9405 |
| net_win_rate | 0.5556 |
| gross_profit_factor | 1.2309 |
| gross_win_rate | 0.5556 |
| sharpe_ratio | -0.3272 |
| sortino_ratio | -0.1008 |
| max_drawdown | 0.3478 |
| cagr | -0.0514 |
| net_avg_win | 78.5571 |
| net_avg_loss | -104.4065 |
| avg_hold_time_bars | 13.9378 |
| exposure | 0.2851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
