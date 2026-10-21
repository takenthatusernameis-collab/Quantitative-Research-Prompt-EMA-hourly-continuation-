# EMA Hourly Continuation — SHIB/USDT P12_34

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.7646 |
| net_win_rate | 0.5206 |
| gross_profit_factor | 1.0833 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -1.9672 |
| sortino_ratio | -0.6558 |
| max_drawdown | 0.5405 |
| cagr | -0.2587 |
| net_avg_win | 61.7398 |
| net_avg_loss | -87.6904 |
| avg_hold_time_bars | 6.7060 |
| exposure | 0.1628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
