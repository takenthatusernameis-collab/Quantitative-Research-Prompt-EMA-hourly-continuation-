# EMA Hourly Continuation — DOGE/USDT P34_144

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6575 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -2.2194 |
| sortino_ratio | -0.5784 |
| max_drawdown | 0.5189 |
| cagr | -0.2322 |
| net_avg_win | 59.3020 |
| net_avg_loss | -79.5504 |
| avg_hold_time_bars | 25.1582 |
| exposure | 0.3831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
