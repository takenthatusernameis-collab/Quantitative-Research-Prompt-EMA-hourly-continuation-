# EMA Hourly Continuation — RENDER/USDT P20_200

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 1.0390 |
| net_win_rate | 0.5496 |
| gross_profit_factor | 1.2000 |
| gross_win_rate | 0.5496 |
| sharpe_ratio | 0.2520 |
| sortino_ratio | 0.0612 |
| max_drawdown | 0.1169 |
| cagr | 0.0213 |
| net_avg_win | 93.3246 |
| net_avg_loss | -109.6039 |
| avg_hold_time_bars | 50.0207 |
| exposure | 0.6389 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
