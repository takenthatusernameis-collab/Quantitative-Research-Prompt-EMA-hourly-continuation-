# EMA Hourly Continuation — ATOM/USDT P100_200

**Symbol:** ATOM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.7314 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -1.4655 |
| sortino_ratio | -0.3268 |
| max_drawdown | 0.3196 |
| cagr | -0.1392 |
| net_avg_win | 71.1675 |
| net_avg_loss | -95.7144 |
| avg_hold_time_bars | 13.1612 |
| exposure | 0.1448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
