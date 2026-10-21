# EMA Hourly Continuation — RPL/USDT P144_200

**Symbol:** RPL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.6966 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9601 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -1.7201 |
| sortino_ratio | -0.3896 |
| max_drawdown | 0.3886 |
| cagr | -0.1640 |
| net_avg_win | 67.3042 |
| net_avg_loss | -94.3337 |
| avg_hold_time_bars | 7.8247 |
| exposure | 0.0889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
