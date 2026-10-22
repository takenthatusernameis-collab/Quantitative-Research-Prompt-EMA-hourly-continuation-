# EMA Hourly Continuation — ICP/USDT P12_100

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6358 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9285 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -3.5750 |
| sortino_ratio | -1.2408 |
| max_drawdown | 0.7773 |
| cagr | -0.4434 |
| net_avg_win | 47.1942 |
| net_avg_loss | -66.7335 |
| avg_hold_time_bars | 22.6312 |
| exposure | 0.6193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
