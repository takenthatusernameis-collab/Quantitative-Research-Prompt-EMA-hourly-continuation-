# EMA Hourly Continuation — XCN/USDT P26_34

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 165 |
| net_profit_factor | 0.7511 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.0843 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.1395 |
| sortino_ratio | -0.2111 |
| max_drawdown | 0.2742 |
| cagr | -0.0918 |
| net_avg_win | 75.3347 |
| net_avg_loss | -109.1925 |
| avg_hold_time_bars | 5.8242 |
| exposure | 0.0437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
