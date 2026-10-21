# EMA Hourly Continuation — JTO/USDT P12_100

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.7862 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9224 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -1.7836 |
| sortino_ratio | -0.5619 |
| max_drawdown | 0.5426 |
| cagr | -0.2290 |
| net_avg_win | 75.6924 |
| net_avg_loss | -87.2833 |
| avg_hold_time_bars | 25.2061 |
| exposure | 0.5614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
