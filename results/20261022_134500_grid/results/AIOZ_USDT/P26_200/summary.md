# EMA Hourly Continuation — AIOZ/USDT P26_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6490 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8701 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -3.1582 |
| sortino_ratio | -0.9444 |
| max_drawdown | 0.7169 |
| cagr | -0.3597 |
| net_avg_win | 60.4531 |
| net_avg_loss | -79.2952 |
| avg_hold_time_bars | 27.7254 |
| exposure | 0.5646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
