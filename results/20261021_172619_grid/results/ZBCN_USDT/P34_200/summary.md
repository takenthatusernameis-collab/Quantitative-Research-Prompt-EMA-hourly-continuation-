# EMA Hourly Continuation — ZBCN/USDT P34_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.9263 |
| net_win_rate | 0.5181 |
| gross_profit_factor | 1.0651 |
| gross_win_rate | 0.5181 |
| sharpe_ratio | -0.4325 |
| sortino_ratio | -0.1188 |
| max_drawdown | 0.2855 |
| cagr | -0.0576 |
| net_avg_win | 92.0077 |
| net_avg_loss | -106.7936 |
| avg_hold_time_bars | 24.9192 |
| exposure | 0.4139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
