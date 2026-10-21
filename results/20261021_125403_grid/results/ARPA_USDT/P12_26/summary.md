# EMA Hourly Continuation — ARPA/USDT P12_26

**Symbol:** ARPA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.6588 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9768 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -4.0291 |
| sortino_ratio | -1.4867 |
| max_drawdown | 0.8224 |
| cagr | -0.4941 |
| net_avg_win | 49.6794 |
| net_avg_loss | -69.5242 |
| avg_hold_time_bars | 5.5805 |
| exposure | 0.1679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
