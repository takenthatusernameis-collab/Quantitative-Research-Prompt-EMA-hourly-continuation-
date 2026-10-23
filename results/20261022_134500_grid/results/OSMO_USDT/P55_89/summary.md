# EMA Hourly Continuation — OSMO/USDT P55_89

**Symbol:** OSMO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.4178 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.7980 |
| gross_win_rate | 0.4141 |
| sharpe_ratio | -7.3918 |
| sortino_ratio | -2.6545 |
| max_drawdown | 0.9619 |
| cagr | -0.7267 |
| net_avg_win | 26.9586 |
| net_avg_loss | -43.0117 |
| avg_hold_time_bars | 4.7359 |
| exposure | 0.1378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
