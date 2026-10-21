# EMA Hourly Continuation — XCN/USDT P50_200

**Symbol:** XCN/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.6802 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8365 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -2.2457 |
| sortino_ratio | -0.5644 |
| max_drawdown | 0.4913 |
| cagr | -0.2299 |
| net_avg_win | 71.5595 |
| net_avg_loss | -87.4652 |
| avg_hold_time_bars | 27.4476 |
| exposure | 0.3930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
