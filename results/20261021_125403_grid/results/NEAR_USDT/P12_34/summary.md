# EMA Hourly Continuation — NEAR/USDT P12_34

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.8431 |
| net_win_rate | 0.5221 |
| gross_profit_factor | 1.0816 |
| gross_win_rate | 0.5221 |
| sharpe_ratio | -1.1939 |
| sortino_ratio | -0.4006 |
| max_drawdown | 0.4192 |
| cagr | -0.1703 |
| net_avg_win | 71.0783 |
| net_avg_loss | -92.1165 |
| avg_hold_time_bars | 7.0351 |
| exposure | 0.1733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
