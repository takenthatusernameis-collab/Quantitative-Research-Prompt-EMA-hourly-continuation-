# EMA Hourly Continuation — ACE/USDT P20_200

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8220 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0187 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.1362 |
| sortino_ratio | -0.3129 |
| max_drawdown | 0.3694 |
| cagr | -0.1360 |
| net_avg_win | 75.3459 |
| net_avg_loss | -93.6489 |
| avg_hold_time_bars | 36.4706 |
| exposure | 0.6173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
