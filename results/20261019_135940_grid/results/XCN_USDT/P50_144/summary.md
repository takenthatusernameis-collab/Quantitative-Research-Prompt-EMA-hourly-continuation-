# EMA Hourly Continuation — XCN/USDT P50_144

**Symbol:** XCN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.4681 |
| net_win_rate | 0.4205 |
| gross_profit_factor | 0.8137 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -6.2740 |
| sortino_ratio | -2.2298 |
| max_drawdown | 0.9377 |
| cagr | -0.6637 |
| net_avg_win | 30.8282 |
| net_avg_loss | -47.7805 |
| avg_hold_time_bars | 10.1417 |
| exposure | 0.2927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
