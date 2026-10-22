# EMA Hourly Continuation — UMA/USDT P8_144

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.8101 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.3221 |
| sortino_ratio | -0.4066 |
| max_drawdown | 0.4140 |
| cagr | -0.1724 |
| net_avg_win | 68.9768 |
| net_avg_loss | -87.3845 |
| avg_hold_time_bars | 32.8766 |
| exposure | 0.6904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
