# EMA Hourly Continuation — KCS/USDT P55_144

**Symbol:** KCS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.5354 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9046 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -3.1560 |
| sortino_ratio | -0.8057 |
| max_drawdown | 0.6096 |
| cagr | -0.3075 |
| net_avg_win | 45.9791 |
| net_avg_loss | -79.0770 |
| avg_hold_time_bars | 19.0984 |
| exposure | 0.2735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
