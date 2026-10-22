# EMA Hourly Continuation — DOGE/USDT P55_144

**Symbol:** DOGE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.5757 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9732 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -3.9728 |
| sortino_ratio | -1.2336 |
| max_drawdown | 0.7826 |
| cagr | -0.4460 |
| net_avg_win | 45.7940 |
| net_avg_loss | -71.4402 |
| avg_hold_time_bars | 11.0992 |
| exposure | 0.2442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
