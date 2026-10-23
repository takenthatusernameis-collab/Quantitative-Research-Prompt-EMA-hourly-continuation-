# EMA Hourly Continuation — DEEP/USDT P34_200

**Symbol:** DEEP/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.7887 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0080 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.2622 |
| sortino_ratio | -0.3161 |
| max_drawdown | 0.2887 |
| cagr | -0.1418 |
| net_avg_win | 76.7573 |
| net_avg_loss | -99.6397 |
| avg_hold_time_bars | 37.7333 |
| exposure | 0.5448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
