# EMA Hourly Continuation — IOTX/USDT P26_55

**Symbol:** IOTX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.5501 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 1.0077 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -7.2501 |
| sortino_ratio | -3.1597 |
| max_drawdown | 0.9795 |
| cagr | -0.7835 |
| net_avg_win | 27.8235 |
| net_avg_loss | -42.0692 |
| avg_hold_time_bars | 4.2429 |
| exposure | 0.1826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
