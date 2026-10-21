# EMA Hourly Continuation — ZRO/USDT P12_144

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.9161 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0508 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -0.4490 |
| sortino_ratio | -0.1238 |
| max_drawdown | 0.1622 |
| cagr | -0.0598 |
| net_avg_win | 82.9849 |
| net_avg_loss | -96.0467 |
| avg_hold_time_bars | 38.8889 |
| exposure | 0.6510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
