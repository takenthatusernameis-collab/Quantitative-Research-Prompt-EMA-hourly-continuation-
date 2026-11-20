# EMA Hourly Continuation — P2P/USDT P21_26

**Symbol:** P2P/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1096 |
| net_profit_factor | 0.1895 |
| net_win_rate | 0.2482 |
| gross_profit_factor | 0.4604 |
| gross_win_rate | 0.2582 |
| sharpe_ratio | -15.9359 |
| sortino_ratio | -7.6758 |
| max_drawdown | 1.0000 |
| cagr | -0.9817 |
| net_avg_win | 8.5945 |
| net_avg_loss | -14.9724 |
| avg_hold_time_bars | 2.8285 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
