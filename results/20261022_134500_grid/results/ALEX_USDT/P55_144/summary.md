# EMA Hourly Continuation — ALEX/USDT P55_144

**Symbol:** ALEX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.5170 |
| net_win_rate | 0.4055 |
| gross_profit_factor | 0.7447 |
| gross_win_rate | 0.4081 |
| sharpe_ratio | -4.4433 |
| sortino_ratio | -1.2342 |
| max_drawdown | 0.7851 |
| cagr | -0.4487 |
| net_avg_win | 51.5747 |
| net_avg_loss | -68.0608 |
| avg_hold_time_bars | 15.7783 |
| exposure | 0.2847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
