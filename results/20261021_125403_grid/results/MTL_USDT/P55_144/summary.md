# EMA Hourly Continuation — MTL/USDT P55_144

**Symbol:** MTL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6209 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8469 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -2.6482 |
| sortino_ratio | -0.6920 |
| max_drawdown | 0.5693 |
| cagr | -0.2725 |
| net_avg_win | 57.5651 |
| net_avg_loss | -80.4140 |
| avg_hold_time_bars | 18.7515 |
| exposure | 0.2868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
