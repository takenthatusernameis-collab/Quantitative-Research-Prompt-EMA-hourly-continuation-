# EMA Hourly Continuation — CTSI/USDT P144_200

**Symbol:** CTSI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.6482 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9321 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -2.3375 |
| sortino_ratio | -0.5327 |
| max_drawdown | 0.4707 |
| cagr | -0.2173 |
| net_avg_win | 70.5724 |
| net_avg_loss | -97.4923 |
| avg_hold_time_bars | 5.7520 |
| exposure | 0.0664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
