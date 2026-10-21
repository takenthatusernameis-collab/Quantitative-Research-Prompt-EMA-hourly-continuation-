# EMA Hourly Continuation — ID/USDT P89_100

**Symbol:** ID/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.7357 |
| net_win_rate | 0.5320 |
| gross_profit_factor | 1.1335 |
| gross_win_rate | 0.5320 |
| sharpe_ratio | -1.3448 |
| sortino_ratio | -0.2761 |
| max_drawdown | 0.2883 |
| cagr | -0.1185 |
| net_avg_win | 70.2453 |
| net_avg_loss | -108.5416 |
| avg_hold_time_bars | 5.0887 |
| exposure | 0.0467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
