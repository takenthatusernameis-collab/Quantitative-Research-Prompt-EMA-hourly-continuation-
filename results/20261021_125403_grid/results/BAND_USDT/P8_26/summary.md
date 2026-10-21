# EMA Hourly Continuation — BAND/USDT P8_26

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.7319 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0391 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -3.3771 |
| sortino_ratio | -1.4234 |
| max_drawdown | 0.8082 |
| cagr | -0.4791 |
| net_avg_win | 50.8663 |
| net_avg_loss | -69.5035 |
| avg_hold_time_bars | 6.4584 |
| exposure | 0.2531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
