# EMA Hourly Continuation — RPL/USDT P26_200

**Symbol:** RPL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8876 |
| net_win_rate | 0.5341 |
| gross_profit_factor | 1.1910 |
| gross_win_rate | 0.5426 |
| sharpe_ratio | -0.6516 |
| sortino_ratio | -0.1731 |
| max_drawdown | 0.2621 |
| cagr | -0.0821 |
| net_avg_win | 81.6033 |
| net_avg_loss | -105.3895 |
| avg_hold_time_bars | 37.6250 |
| exposure | 0.5994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
