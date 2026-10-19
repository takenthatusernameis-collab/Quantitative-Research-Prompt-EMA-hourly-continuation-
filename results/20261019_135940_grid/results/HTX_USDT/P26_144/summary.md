# EMA Hourly Continuation — HTX/USDT P26_144

**Symbol:** HTX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.4057 |
| net_win_rate | 0.3560 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4061 |
| sharpe_ratio | -9.0538 |
| sortino_ratio | -3.0911 |
| max_drawdown | 0.9847 |
| cagr | -0.8042 |
| net_avg_win | 33.7407 |
| net_avg_loss | -45.9745 |
| avg_hold_time_bars | 20.0751 |
| exposure | 0.5078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
