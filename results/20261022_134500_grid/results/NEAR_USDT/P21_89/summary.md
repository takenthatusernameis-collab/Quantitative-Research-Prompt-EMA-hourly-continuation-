# EMA Hourly Continuation — NEAR/USDT P21_89

**Symbol:** NEAR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.6394 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.9534 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -4.1943 |
| sortino_ratio | -1.5311 |
| max_drawdown | 0.8526 |
| cagr | -0.5263 |
| net_avg_win | 46.6274 |
| net_avg_loss | -65.0479 |
| avg_hold_time_bars | 12.0644 |
| exposure | 0.3745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
