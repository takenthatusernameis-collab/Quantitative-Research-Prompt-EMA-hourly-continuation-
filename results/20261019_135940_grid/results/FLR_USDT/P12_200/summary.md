# EMA Hourly Continuation — FLR/USDT P12_200

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.5943 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9363 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -4.0391 |
| sortino_ratio | -1.3741 |
| max_drawdown | 0.8254 |
| cagr | -0.4916 |
| net_avg_win | 42.1501 |
| net_avg_loss | -65.3946 |
| avg_hold_time_bars | 24.6588 |
| exposure | 0.6635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
