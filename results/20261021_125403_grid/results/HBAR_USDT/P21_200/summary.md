# EMA Hourly Continuation — HBAR/USDT P21_200

**Symbol:** HBAR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.7952 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9696 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -1.1259 |
| sortino_ratio | -0.2727 |
| max_drawdown | 0.3130 |
| cagr | -0.1189 |
| net_avg_win | 73.9336 |
| net_avg_loss | -92.3262 |
| avg_hold_time_bars | 49.5122 |
| exposure | 0.6459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
