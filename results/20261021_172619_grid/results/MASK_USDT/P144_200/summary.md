# EMA Hourly Continuation — MASK/USDT P144_200

**Symbol:** MASK/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.5739 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.8861 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -2.6628 |
| sortino_ratio | -0.6068 |
| max_drawdown | 0.5297 |
| cagr | -0.2451 |
| net_avg_win | 56.8275 |
| net_avg_loss | -89.3448 |
| avg_hold_time_bars | 7.2174 |
| exposure | 0.0830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
