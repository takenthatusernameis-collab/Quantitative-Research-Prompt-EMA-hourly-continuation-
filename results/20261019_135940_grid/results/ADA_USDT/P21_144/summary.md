# EMA Hourly Continuation — ADA/USDT P21_144

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.6108 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9524 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -3.5158 |
| sortino_ratio | -1.0728 |
| max_drawdown | 0.7387 |
| cagr | -0.4079 |
| net_avg_win | 50.5928 |
| net_avg_loss | -75.5133 |
| avg_hold_time_bars | 24.4601 |
| exposure | 0.5292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
