# EMA Hourly Continuation — SHR/USDT P21_89

**Symbol:** SHR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1042 |
| net_profit_factor | 0.4073 |
| net_win_rate | 0.3407 |
| gross_profit_factor | 0.5650 |
| gross_win_rate | 0.3407 |
| sharpe_ratio | -9.4654 |
| sortino_ratio | -4.2592 |
| max_drawdown | 0.9944 |
| cagr | -0.8713 |
| net_avg_win | 19.2472 |
| net_avg_loss | -24.4192 |
| avg_hold_time_bars | 6.7889 |
| exposure | 0.3201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
