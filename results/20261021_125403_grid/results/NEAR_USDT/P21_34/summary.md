# EMA Hourly Continuation — NEAR/USDT P21_34

**Symbol:** NEAR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.8184 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.0843 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -0.9151 |
| sortino_ratio | -0.2079 |
| max_drawdown | 0.2612 |
| cagr | -0.0916 |
| net_avg_win | 74.3529 |
| net_avg_loss | -100.0898 |
| avg_hold_time_bars | 5.6855 |
| exposure | 0.0641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
