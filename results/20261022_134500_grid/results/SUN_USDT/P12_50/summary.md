# EMA Hourly Continuation — SUN/USDT P12_50

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 929 |
| net_profit_factor | 0.3169 |
| net_win_rate | 0.3832 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -10.9214 |
| sortino_ratio | -4.7373 |
| max_drawdown | 0.9981 |
| cagr | -0.9166 |
| net_avg_win | 13.0067 |
| net_avg_loss | -25.4998 |
| avg_hold_time_bars | 9.1712 |
| exposure | 0.3856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
