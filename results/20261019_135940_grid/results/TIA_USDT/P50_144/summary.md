# EMA Hourly Continuation — TIA/USDT P50_144

**Symbol:** TIA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6217 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8676 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -3.2813 |
| sortino_ratio | -0.9954 |
| max_drawdown | 0.7050 |
| cagr | -0.3791 |
| net_avg_win | 53.0937 |
| net_avg_loss | -73.7857 |
| avg_hold_time_bars | 13.3777 |
| exposure | 0.2834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
