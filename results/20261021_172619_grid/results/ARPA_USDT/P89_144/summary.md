# EMA Hourly Continuation — ARPA/USDT P89_144

**Symbol:** ARPA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.5367 |
| net_win_rate | 0.4310 |
| gross_profit_factor | 0.7707 |
| gross_win_rate | 0.4310 |
| sharpe_ratio | -3.7534 |
| sortino_ratio | -0.9951 |
| max_drawdown | 0.6896 |
| cagr | -0.3680 |
| net_avg_win | 52.9497 |
| net_avg_loss | -74.7477 |
| avg_hold_time_bars | 7.7615 |
| exposure | 0.1222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
