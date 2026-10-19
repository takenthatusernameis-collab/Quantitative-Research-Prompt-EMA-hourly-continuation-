# EMA Hourly Continuation — INJ/USDT P100_144

**Symbol:** INJ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.4674 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.7751 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -5.4635 |
| sortino_ratio | -1.7626 |
| max_drawdown | 0.8917 |
| cagr | -0.5765 |
| net_avg_win | 34.4987 |
| net_avg_loss | -56.2937 |
| avg_hold_time_bars | 3.6865 |
| exposure | 0.0871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
