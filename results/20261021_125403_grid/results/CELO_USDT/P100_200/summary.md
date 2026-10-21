# EMA Hourly Continuation — CELO/USDT P100_200

**Symbol:** CELO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.7158 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.6881 |
| sortino_ratio | -0.3931 |
| max_drawdown | 0.3988 |
| cagr | -0.1655 |
| net_avg_win | 71.5403 |
| net_avg_loss | -93.4246 |
| avg_hold_time_bars | 11.9625 |
| exposure | 0.1445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
