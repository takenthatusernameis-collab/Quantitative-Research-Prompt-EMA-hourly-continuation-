# EMA Hourly Continuation — PYTH/USDT P12_200

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.9814 |
| net_win_rate | 0.5289 |
| gross_profit_factor | 1.1056 |
| gross_win_rate | 0.5289 |
| sharpe_ratio | -0.0423 |
| sortino_ratio | -0.0095 |
| max_drawdown | 0.2316 |
| cagr | -0.0089 |
| net_avg_win | 91.3128 |
| net_avg_loss | -104.4738 |
| avg_hold_time_bars | 70.6446 |
| exposure | 0.7771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
