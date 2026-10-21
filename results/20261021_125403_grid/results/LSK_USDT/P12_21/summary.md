# EMA Hourly Continuation — LSK/USDT P12_21

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.6397 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 1.0757 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -3.7110 |
| sortino_ratio | -1.2621 |
| max_drawdown | 0.7816 |
| cagr | -0.4399 |
| net_avg_win | 49.3258 |
| net_avg_loss | -75.4663 |
| avg_hold_time_bars | 5.2706 |
| exposure | 0.1337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
