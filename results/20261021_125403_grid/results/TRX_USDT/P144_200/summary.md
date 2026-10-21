# EMA Hourly Continuation — TRX/USDT P144_200

**Symbol:** TRX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 132 |
| net_profit_factor | 0.4194 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0131 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -2.8948 |
| sortino_ratio | -0.4866 |
| max_drawdown | 0.4484 |
| cagr | -0.2038 |
| net_avg_win | 46.9849 |
| net_avg_loss | -115.4714 |
| avg_hold_time_bars | 8.7652 |
| exposure | 0.0526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
