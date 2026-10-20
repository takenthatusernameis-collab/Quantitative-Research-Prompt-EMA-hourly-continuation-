# EMA Hourly Continuation — XYO/USDT P12_200

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.5243 |
| net_win_rate | 0.4353 |
| gross_profit_factor | 0.8142 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -4.9743 |
| sortino_ratio | -1.6406 |
| max_drawdown | 0.8704 |
| cagr | -0.5463 |
| net_avg_win | 39.3420 |
| net_avg_loss | -57.8300 |
| avg_hold_time_bars | 27.3165 |
| exposure | 0.6873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
