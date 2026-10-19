# EMA Hourly Continuation — FLR/USDT P55_100

**Symbol:** FLR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.4045 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.8368 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -8.1217 |
| sortino_ratio | -3.1456 |
| max_drawdown | 0.9816 |
| cagr | -0.7951 |
| net_avg_win | 21.2961 |
| net_avg_loss | -37.7959 |
| avg_hold_time_bars | 4.4059 |
| exposure | 0.1500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
