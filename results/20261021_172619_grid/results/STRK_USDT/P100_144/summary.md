# EMA Hourly Continuation — STRK/USDT P100_144

**Symbol:** STRK/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.9159 |
| net_win_rate | 0.5415 |
| gross_profit_factor | 1.1805 |
| gross_win_rate | 0.5415 |
| sharpe_ratio | -0.4110 |
| sortino_ratio | -0.0901 |
| max_drawdown | 0.2245 |
| cagr | -0.0429 |
| net_avg_win | 91.6613 |
| net_avg_loss | -118.1880 |
| avg_hold_time_bars | 6.2096 |
| exposure | 0.0646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
