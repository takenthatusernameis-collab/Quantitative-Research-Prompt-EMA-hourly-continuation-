# EMA Hourly Continuation — DASH/USDT P144_200

**Symbol:** DASH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.2790 |
| net_win_rate | 0.4086 |
| gross_profit_factor | 0.7054 |
| gross_win_rate | 0.4312 |
| sharpe_ratio | -6.5132 |
| sortino_ratio | -1.9383 |
| max_drawdown | 0.9177 |
| cagr | -0.6263 |
| net_avg_win | 19.5771 |
| net_avg_loss | -48.4707 |
| avg_hold_time_bars | 3.3025 |
| exposure | 0.0665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
