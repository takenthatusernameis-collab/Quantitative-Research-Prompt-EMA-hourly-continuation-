# EMA Hourly Continuation — STRAX/USDT P12_55

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6687 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -3.7369 |
| sortino_ratio | -1.3979 |
| max_drawdown | 0.8125 |
| cagr | -0.4753 |
| net_avg_win | 50.1452 |
| net_avg_loss | -65.9780 |
| avg_hold_time_bars | 12.2049 |
| exposure | 0.3839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
