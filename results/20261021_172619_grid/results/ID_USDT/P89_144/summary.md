# EMA Hourly Continuation — ID/USDT P89_144

**Symbol:** ID/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7322 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9872 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.5948 |
| sortino_ratio | -0.3973 |
| max_drawdown | 0.3687 |
| cagr | -0.1667 |
| net_avg_win | 66.3419 |
| net_avg_loss | -91.2013 |
| avg_hold_time_bars | 8.8020 |
| exposure | 0.1207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
