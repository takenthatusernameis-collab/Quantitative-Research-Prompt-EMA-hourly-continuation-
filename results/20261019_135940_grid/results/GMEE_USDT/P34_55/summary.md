# EMA Hourly Continuation — GMEE/USDT P34_55

**Symbol:** GMEE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 887 |
| net_profit_factor | 0.3359 |
| net_win_rate | 0.3946 |
| gross_profit_factor | 0.5642 |
| gross_win_rate | 0.4081 |
| sharpe_ratio | -8.9054 |
| sortino_ratio | -3.7535 |
| max_drawdown | 0.9907 |
| cagr | -0.8440 |
| net_avg_win | 14.3167 |
| net_avg_loss | -27.7779 |
| avg_hold_time_bars | 3.7001 |
| exposure | 0.1492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
