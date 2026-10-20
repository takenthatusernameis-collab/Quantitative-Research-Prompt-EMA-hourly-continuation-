# EMA Hourly Continuation — MANTA/USDT P55_89

**Symbol:** MANTA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.4627 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.7915 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -6.3345 |
| sortino_ratio | -2.3161 |
| max_drawdown | 0.9417 |
| cagr | -0.6760 |
| net_avg_win | 28.1337 |
| net_avg_loss | -45.9642 |
| avg_hold_time_bars | 4.6831 |
| exposure | 0.1424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
