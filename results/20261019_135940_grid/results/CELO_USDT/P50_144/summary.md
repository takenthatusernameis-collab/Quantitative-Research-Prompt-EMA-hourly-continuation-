# EMA Hourly Continuation — CELO/USDT P50_144

**Symbol:** CELO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.7574 |
| net_win_rate | 0.5210 |
| gross_profit_factor | 1.1216 |
| gross_win_rate | 0.5276 |
| sharpe_ratio | -1.8164 |
| sortino_ratio | -0.5500 |
| max_drawdown | 0.4913 |
| cagr | -0.2265 |
| net_avg_win | 63.0673 |
| net_avg_loss | -90.5627 |
| avg_hold_time_bars | 14.0552 |
| exposure | 0.2881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
