# EMA Hourly Continuation — CHZ/USDT P144_200

**Symbol:** CHZ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.4314 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8206 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -4.2325 |
| sortino_ratio | -1.1128 |
| max_drawdown | 0.7541 |
| cagr | -0.4201 |
| net_avg_win | 35.8044 |
| net_avg_loss | -69.0100 |
| avg_hold_time_bars | 4.9713 |
| exposure | 0.0786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
