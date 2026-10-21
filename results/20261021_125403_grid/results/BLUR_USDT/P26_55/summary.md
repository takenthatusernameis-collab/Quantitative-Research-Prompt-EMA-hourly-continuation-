# EMA Hourly Continuation — BLUR/USDT P26_55

**Symbol:** BLUR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.7163 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 0.9762 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -2.3372 |
| sortino_ratio | -0.7654 |
| max_drawdown | 0.6156 |
| cagr | -0.2962 |
| net_avg_win | 56.8686 |
| net_avg_loss | -78.4861 |
| avg_hold_time_bars | 6.5181 |
| exposure | 0.1548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
