# EMA Hourly Continuation — CTSI/USDT P34_100

**Symbol:** CTSI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.5548 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.8615 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -5.5075 |
| sortino_ratio | -2.0600 |
| max_drawdown | 0.9180 |
| cagr | -0.6251 |
| net_avg_win | 37.6263 |
| net_avg_loss | -51.5035 |
| avg_hold_time_bars | 9.1795 |
| exposure | 0.2929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
