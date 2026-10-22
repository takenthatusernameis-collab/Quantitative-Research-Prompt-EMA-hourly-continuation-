# EMA Hourly Continuation — NEAR/USDT P89_100

**Symbol:** NEAR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.2669 |
| net_win_rate | 0.3891 |
| gross_profit_factor | 0.6827 |
| gross_win_rate | 0.4198 |
| sharpe_ratio | -8.7612 |
| sortino_ratio | -3.0540 |
| max_drawdown | 0.9815 |
| cagr | -0.7958 |
| net_avg_win | 15.6758 |
| net_avg_loss | -37.3992 |
| avg_hold_time_bars | 1.9386 |
| exposure | 0.0516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
