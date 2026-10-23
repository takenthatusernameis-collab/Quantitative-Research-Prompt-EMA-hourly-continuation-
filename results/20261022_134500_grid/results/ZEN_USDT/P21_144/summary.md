# EMA Hourly Continuation — ZEN/USDT P21_144

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7293 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0632 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -2.3854 |
| sortino_ratio | -0.7668 |
| max_drawdown | 0.6422 |
| cagr | -0.3063 |
| net_avg_win | 61.5418 |
| net_avg_loss | -86.6943 |
| avg_hold_time_bars | 22.4875 |
| exposure | 0.5305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
