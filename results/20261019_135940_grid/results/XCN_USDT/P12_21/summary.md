# EMA Hourly Continuation — XCN/USDT P12_21

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1761 |
| net_profit_factor | 0.2043 |
| net_win_rate | 0.3311 |
| gross_profit_factor | 0.5375 |
| gross_win_rate | 0.3646 |
| sharpe_ratio | -17.9929 |
| sortino_ratio | -10.8492 |
| max_drawdown | 1.0000 |
| cagr | -0.9968 |
| net_avg_win | 4.4047 |
| net_avg_loss | -10.6689 |
| avg_hold_time_bars | 2.1352 |
| exposure | 0.1709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
