# EMA Hourly Continuation — AMP/USDT P55_200

**Symbol:** AMP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6516 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8356 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -2.5978 |
| sortino_ratio | -0.7258 |
| max_drawdown | 0.5989 |
| cagr | -0.2846 |
| net_avg_win | 60.1039 |
| net_avg_loss | -77.7437 |
| avg_hold_time_bars | 21.0233 |
| exposure | 0.3698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
