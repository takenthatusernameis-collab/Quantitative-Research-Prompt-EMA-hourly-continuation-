# EMA Hourly Continuation — ARKM/USDT P8_200

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7235 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9241 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -2.0080 |
| sortino_ratio | -0.5275 |
| max_drawdown | 0.5165 |
| cagr | -0.2222 |
| net_avg_win | 73.7664 |
| net_avg_loss | -91.9798 |
| avg_hold_time_bars | 51.4457 |
| exposure | 0.8185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
