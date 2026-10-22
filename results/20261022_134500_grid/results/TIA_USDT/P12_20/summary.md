# EMA Hourly Continuation — TIA/USDT P12_20

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1479 |
| net_profit_factor | 0.3462 |
| net_win_rate | 0.4104 |
| gross_profit_factor | 0.7580 |
| gross_win_rate | 0.4314 |
| sharpe_ratio | -12.5938 |
| sortino_ratio | -6.8621 |
| max_drawdown | 0.9999 |
| cagr | -0.9713 |
| net_avg_win | 8.7206 |
| net_avg_loss | -17.5368 |
| avg_hold_time_bars | 2.0014 |
| exposure | 0.1345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
