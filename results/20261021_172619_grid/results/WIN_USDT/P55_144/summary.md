# EMA Hourly Continuation — WIN/USDT P55_144

**Symbol:** WIN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.6898 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9493 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -1.8708 |
| sortino_ratio | -0.4526 |
| max_drawdown | 0.4775 |
| cagr | -0.1882 |
| net_avg_win | 64.7690 |
| net_avg_loss | -90.6511 |
| avg_hold_time_bars | 18.5404 |
| exposure | 0.2402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
