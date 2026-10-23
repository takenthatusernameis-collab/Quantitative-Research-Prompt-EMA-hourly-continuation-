# EMA Hourly Continuation — SQD/USDT P12_21

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1332 |
| net_profit_factor | 0.4805 |
| net_win_rate | 0.4152 |
| gross_profit_factor | 0.9397 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -11.0026 |
| sortino_ratio | -5.7228 |
| max_drawdown | 0.9992 |
| cagr | -0.9470 |
| net_avg_win | 16.7105 |
| net_avg_loss | -24.6893 |
| avg_hold_time_bars | 2.4670 |
| exposure | 0.1545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
