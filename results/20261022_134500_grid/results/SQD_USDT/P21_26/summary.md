# EMA Hourly Continuation — SQD/USDT P21_26

**Symbol:** SQD/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1113 |
| net_profit_factor | 0.4016 |
| net_win_rate | 0.3971 |
| gross_profit_factor | 0.9158 |
| gross_win_rate | 0.4376 |
| sharpe_ratio | -11.5987 |
| sortino_ratio | -5.5765 |
| max_drawdown | 0.9992 |
| cagr | -0.9466 |
| net_avg_win | 15.1738 |
| net_avg_loss | -24.8863 |
| avg_hold_time_bars | 2.1069 |
| exposure | 0.1102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
