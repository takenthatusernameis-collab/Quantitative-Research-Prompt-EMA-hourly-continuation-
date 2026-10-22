# EMA Hourly Continuation — BSV/USDT P100_200

**Symbol:** BSV/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.4559 |
| net_win_rate | 0.4035 |
| gross_profit_factor | 0.7939 |
| gross_win_rate | 0.4167 |
| sharpe_ratio | -5.8890 |
| sortino_ratio | -1.7645 |
| max_drawdown | 0.8914 |
| cagr | -0.5853 |
| net_avg_win | 40.5479 |
| net_avg_loss | -60.1622 |
| avg_hold_time_bars | 8.0702 |
| exposure | 0.1673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
