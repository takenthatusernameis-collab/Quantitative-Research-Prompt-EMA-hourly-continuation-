# EMA Hourly Continuation — RLC/USDT P55_144

**Symbol:** RLC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.5678 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8831 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -3.8034 |
| sortino_ratio | -1.2242 |
| max_drawdown | 0.7820 |
| cagr | -0.4410 |
| net_avg_win | 41.6772 |
| net_avg_loss | -64.3645 |
| avg_hold_time_bars | 10.2375 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
