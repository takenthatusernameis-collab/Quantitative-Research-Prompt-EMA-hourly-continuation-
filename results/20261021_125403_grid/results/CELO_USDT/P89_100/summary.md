# EMA Hourly Continuation — CELO/USDT P89_100

**Symbol:** CELO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 125 |
| net_profit_factor | 0.8307 |
| net_win_rate | 0.5600 |
| gross_profit_factor | 1.2670 |
| gross_win_rate | 0.5600 |
| sharpe_ratio | -0.6301 |
| sortino_ratio | -0.1021 |
| max_drawdown | 0.1788 |
| cagr | -0.0461 |
| net_avg_win | 78.6293 |
| net_avg_loss | -120.4682 |
| avg_hold_time_bars | 4.9680 |
| exposure | 0.0281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
