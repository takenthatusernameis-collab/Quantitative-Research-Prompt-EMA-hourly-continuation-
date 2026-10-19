# EMA Hourly Continuation — XCN/USDT P21_26

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1432 |
| net_profit_factor | 0.1355 |
| net_win_rate | 0.3010 |
| gross_profit_factor | 0.4904 |
| gross_win_rate | 0.3527 |
| sharpe_ratio | -18.4897 |
| sortino_ratio | -10.3449 |
| max_drawdown | 1.0000 |
| cagr | -0.9967 |
| net_avg_win | 3.6377 |
| net_avg_loss | -11.5563 |
| avg_hold_time_bars | 1.8457 |
| exposure | 0.1201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
