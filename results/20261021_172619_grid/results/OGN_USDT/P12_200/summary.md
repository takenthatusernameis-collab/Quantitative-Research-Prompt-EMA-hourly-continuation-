# EMA Hourly Continuation — OGN/USDT P12_200

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7180 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -1.7333 |
| sortino_ratio | -0.4172 |
| max_drawdown | 0.4358 |
| cagr | -0.1753 |
| net_avg_win | 72.6113 |
| net_avg_loss | -88.6517 |
| avg_hold_time_bars | 56.0104 |
| exposure | 0.7325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
