# EMA Hourly Continuation — SKL/USDT P89_200

**Symbol:** SKL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.9832 |
| net_win_rate | 0.5508 |
| gross_profit_factor | 1.2106 |
| gross_win_rate | 0.5508 |
| sharpe_ratio | -0.0321 |
| sortino_ratio | -0.0075 |
| max_drawdown | 0.2023 |
| cagr | -0.0083 |
| net_avg_win | 85.9890 |
| net_avg_loss | -107.2348 |
| avg_hold_time_bars | 17.7578 |
| exposure | 0.2066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
