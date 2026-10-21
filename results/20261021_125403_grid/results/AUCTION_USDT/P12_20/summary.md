# EMA Hourly Continuation — AUCTION/USDT P12_20

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.4635 |
| net_win_rate | 0.4027 |
| gross_profit_factor | 0.7263 |
| gross_win_rate | 0.4066 |
| sharpe_ratio | -6.1793 |
| sortino_ratio | -2.0026 |
| max_drawdown | 0.9103 |
| cagr | -0.6129 |
| net_avg_win | 37.9279 |
| net_avg_loss | -55.1735 |
| avg_hold_time_bars | 5.2198 |
| exposure | 0.1214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
