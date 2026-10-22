# EMA Hourly Continuation — MANTA/USDT P12_26

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.7082 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -3.0697 |
| sortino_ratio | -1.0439 |
| max_drawdown | 0.7226 |
| cagr | -0.3808 |
| net_avg_win | 62.6828 |
| net_avg_loss | -81.3084 |
| avg_hold_time_bars | 5.7385 |
| exposure | 0.1476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
