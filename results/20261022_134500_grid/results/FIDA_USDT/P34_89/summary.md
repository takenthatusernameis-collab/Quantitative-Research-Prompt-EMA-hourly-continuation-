# EMA Hourly Continuation — FIDA/USDT P34_89

**Symbol:** FIDA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.5327 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8489 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -5.2019 |
| sortino_ratio | -1.9379 |
| max_drawdown | 0.9073 |
| cagr | -0.6042 |
| net_avg_win | 32.5937 |
| net_avg_loss | -50.0896 |
| avg_hold_time_bars | 8.1325 |
| exposure | 0.2583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
