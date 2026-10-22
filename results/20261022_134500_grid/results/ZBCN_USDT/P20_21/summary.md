# EMA Hourly Continuation — ZBCN/USDT P20_21

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1268 |
| net_profit_factor | 0.1176 |
| net_win_rate | 0.3186 |
| gross_profit_factor | 0.4474 |
| gross_win_rate | 0.3604 |
| sharpe_ratio | -16.9679 |
| sortino_ratio | -8.9967 |
| max_drawdown | 1.0000 |
| cagr | -0.9941 |
| net_avg_win | 3.2997 |
| net_avg_loss | -13.1169 |
| avg_hold_time_bars | 1.6238 |
| exposure | 0.0953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
