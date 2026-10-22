# EMA Hourly Continuation — G/USDT P12_34

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.6427 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9300 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -3.7639 |
| sortino_ratio | -1.4748 |
| max_drawdown | 0.7774 |
| cagr | -0.4913 |
| net_avg_win | 44.2206 |
| net_avg_loss | -64.6721 |
| avg_hold_time_bars | 7.7291 |
| exposure | 0.2625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
