# EMA Hourly Continuation — P2P/USDT P20_26

**Symbol:** P2P/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1099 |
| net_profit_factor | 0.1867 |
| net_win_rate | 0.2511 |
| gross_profit_factor | 0.4459 |
| gross_win_rate | 0.2602 |
| sharpe_ratio | -15.6789 |
| sortino_ratio | -7.5368 |
| max_drawdown | 0.9999 |
| cagr | -0.9798 |
| net_avg_win | 8.3145 |
| net_avg_loss | -14.9383 |
| avg_hold_time_bars | 2.8571 |
| exposure | 0.1427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
