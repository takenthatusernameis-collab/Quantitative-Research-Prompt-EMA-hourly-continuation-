# EMA Hourly Continuation — CETUS/USDT P50_100

**Symbol:** CETUS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7277 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9268 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.9769 |
| sortino_ratio | -0.5724 |
| max_drawdown | 0.4930 |
| cagr | -0.2321 |
| net_avg_win | 64.9932 |
| net_avg_loss | -83.8599 |
| avg_hold_time_bars | 8.6586 |
| exposure | 0.1618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
