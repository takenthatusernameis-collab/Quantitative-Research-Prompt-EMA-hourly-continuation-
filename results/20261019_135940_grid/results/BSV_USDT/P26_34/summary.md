# EMA Hourly Continuation — BSV/USDT P26_34

**Symbol:** BSV/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1185 |
| net_profit_factor | 0.1615 |
| net_win_rate | 0.3426 |
| gross_profit_factor | 0.6000 |
| gross_win_rate | 0.3975 |
| sharpe_ratio | -15.5638 |
| sortino_ratio | -7.8495 |
| max_drawdown | 1.0000 |
| cagr | -0.9860 |
| net_avg_win | 4.7440 |
| net_avg_loss | -15.3092 |
| avg_hold_time_bars | 2.1848 |
| exposure | 0.1177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
