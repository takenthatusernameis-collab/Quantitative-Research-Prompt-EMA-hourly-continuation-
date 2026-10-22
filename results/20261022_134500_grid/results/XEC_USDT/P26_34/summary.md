# EMA Hourly Continuation — XEC/USDT P26_34

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.2872 |
| net_win_rate | 0.3924 |
| gross_profit_factor | 0.8712 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -13.1033 |
| sortino_ratio | -6.5447 |
| max_drawdown | 0.9998 |
| cagr | -0.9652 |
| net_avg_win | 8.6991 |
| net_avg_loss | -19.5615 |
| avg_hold_time_bars | 2.5593 |
| exposure | 0.1367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
