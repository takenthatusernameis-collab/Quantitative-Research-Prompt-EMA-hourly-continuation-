# EMA Hourly Continuation — BSV/USDT P8_55

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.6475 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -3.8497 |
| sortino_ratio | -1.4706 |
| max_drawdown | 0.8223 |
| cagr | -0.4909 |
| net_avg_win | 45.3035 |
| net_avg_loss | -59.5369 |
| avg_hold_time_bars | 13.5611 |
| exposure | 0.4438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
