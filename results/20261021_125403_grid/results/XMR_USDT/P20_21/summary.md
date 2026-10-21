# EMA Hourly Continuation — XMR/USDT P20_21

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 68 |
| net_profit_factor | 0.5790 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8326 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -1.3747 |
| sortino_ratio | -0.1623 |
| max_drawdown | 0.1904 |
| cagr | -0.0720 |
| net_avg_win | 75.8983 |
| net_avg_loss | -109.8336 |
| avg_hold_time_bars | 3.6176 |
| exposure | 0.0112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
