# EMA Hourly Continuation — ILV/USDT P20_34

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1133 |
| net_profit_factor | 0.3873 |
| net_win_rate | 0.4104 |
| gross_profit_factor | 0.8161 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -10.5566 |
| sortino_ratio | -5.0500 |
| max_drawdown | 0.9983 |
| cagr | -0.9207 |
| net_avg_win | 13.5706 |
| net_avg_loss | -24.3909 |
| avg_hold_time_bars | 2.8111 |
| exposure | 0.1448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
