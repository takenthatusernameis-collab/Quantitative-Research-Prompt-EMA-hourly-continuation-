# EMA Hourly Continuation — POKT/USDT P8_50

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.6588 |
| net_win_rate | 0.4407 |
| gross_profit_factor | 0.8426 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -4.1425 |
| sortino_ratio | -1.5934 |
| max_drawdown | 0.8459 |
| cagr | -0.5214 |
| net_avg_win | 49.8416 |
| net_avg_loss | -59.6142 |
| avg_hold_time_bars | 11.6078 |
| exposure | 0.3898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
