# EMA Hourly Continuation — IOTX/USDT P26_34

**Symbol:** IOTX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.3128 |
| net_win_rate | 0.3711 |
| gross_profit_factor | 0.7835 |
| gross_win_rate | 0.4133 |
| sharpe_ratio | -12.8427 |
| sortino_ratio | -6.0954 |
| max_drawdown | 0.9996 |
| cagr | -0.9573 |
| net_avg_win | 11.4925 |
| net_avg_loss | -21.6802 |
| avg_hold_time_bars | 2.3721 |
| exposure | 0.1150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
