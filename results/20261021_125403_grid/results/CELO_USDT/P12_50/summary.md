# EMA Hourly Continuation — CELO/USDT P12_50

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.7131 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.9277 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -3.1139 |
| sortino_ratio | -1.1594 |
| max_drawdown | 0.7481 |
| cagr | -0.4124 |
| net_avg_win | 56.6676 |
| net_avg_loss | -71.3169 |
| avg_hold_time_bars | 11.1489 |
| exposure | 0.3456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
