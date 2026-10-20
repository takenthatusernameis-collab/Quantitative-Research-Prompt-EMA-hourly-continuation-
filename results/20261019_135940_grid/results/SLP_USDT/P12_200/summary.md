# EMA Hourly Continuation — SLP/USDT P12_200

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.6377 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9103 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -3.2811 |
| sortino_ratio | -1.0023 |
| max_drawdown | 0.7152 |
| cagr | -0.3814 |
| net_avg_win | 55.7912 |
| net_avg_loss | -76.7297 |
| avg_hold_time_bars | 33.9027 |
| exposure | 0.7289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
