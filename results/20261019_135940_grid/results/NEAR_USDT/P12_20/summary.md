# EMA Hourly Continuation — NEAR/USDT P12_20

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1523 |
| net_profit_factor | 0.3781 |
| net_win_rate | 0.4077 |
| gross_profit_factor | 0.8905 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -13.3739 |
| sortino_ratio | -7.4036 |
| max_drawdown | 0.9999 |
| cagr | -0.9794 |
| net_avg_win | 9.7916 |
| net_avg_loss | -17.8271 |
| avg_hold_time_bars | 2.0578 |
| exposure | 0.1425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
