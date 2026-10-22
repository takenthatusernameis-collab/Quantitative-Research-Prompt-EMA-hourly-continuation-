# EMA Hourly Continuation — CARV/USDT P100_144

**Symbol:** CARV/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.6110 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8706 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -2.3930 |
| sortino_ratio | -0.5528 |
| max_drawdown | 0.4205 |
| cagr | -0.2233 |
| net_avg_win | 63.6176 |
| net_avg_loss | -92.0349 |
| avg_hold_time_bars | 7.2133 |
| exposure | 0.0856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
