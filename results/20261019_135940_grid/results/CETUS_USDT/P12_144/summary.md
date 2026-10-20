# EMA Hourly Continuation — CETUS/USDT P12_144

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.8997 |
| net_win_rate | 0.5487 |
| gross_profit_factor | 1.2103 |
| gross_win_rate | 0.5487 |
| sharpe_ratio | -0.6652 |
| sortino_ratio | -0.1849 |
| max_drawdown | 0.3866 |
| cagr | -0.0894 |
| net_avg_win | 88.1745 |
| net_avg_loss | -119.1650 |
| avg_hold_time_bars | 42.4795 |
| exposure | 0.7497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
