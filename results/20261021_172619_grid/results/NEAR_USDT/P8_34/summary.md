# EMA Hourly Continuation — NEAR/USDT P8_34

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.8445 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0650 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.4103 |
| sortino_ratio | -0.5365 |
| max_drawdown | 0.5126 |
| cagr | -0.2211 |
| net_avg_win | 70.0980 |
| net_avg_loss | -88.6568 |
| avg_hold_time_bars | 8.4077 |
| exposure | 0.2671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
