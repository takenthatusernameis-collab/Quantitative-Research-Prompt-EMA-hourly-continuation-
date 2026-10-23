# EMA Hourly Continuation — ID/USDT P100_144

**Symbol:** ID/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.4072 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.7752 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -5.2826 |
| sortino_ratio | -1.5737 |
| max_drawdown | 0.8629 |
| cagr | -0.5452 |
| net_avg_win | 30.0864 |
| net_avg_loss | -57.3089 |
| avg_hold_time_bars | 4.9468 |
| exposure | 0.1010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
