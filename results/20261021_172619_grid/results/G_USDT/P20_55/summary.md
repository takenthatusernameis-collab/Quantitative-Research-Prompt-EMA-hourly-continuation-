# EMA Hourly Continuation — G/USDT P20_55

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -3.7654 |
| sortino_ratio | -1.3317 |
| max_drawdown | 0.7529 |
| cagr | -0.4568 |
| net_avg_win | 49.1035 |
| net_avg_loss | -68.3843 |
| avg_hold_time_bars | 10.1283 |
| exposure | 0.2823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
