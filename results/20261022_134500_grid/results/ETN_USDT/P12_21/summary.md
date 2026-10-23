# EMA Hourly Continuation — ETN/USDT P12_21

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1280 |
| net_profit_factor | 0.1891 |
| net_win_rate | 0.2781 |
| gross_profit_factor | 0.3413 |
| gross_win_rate | 0.3008 |
| sharpe_ratio | -18.7437 |
| sortino_ratio | -10.6202 |
| max_drawdown | 1.0000 |
| cagr | -0.9967 |
| net_avg_win | 6.5518 |
| net_avg_loss | -13.3467 |
| avg_hold_time_bars | 2.5992 |
| exposure | 0.1807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
