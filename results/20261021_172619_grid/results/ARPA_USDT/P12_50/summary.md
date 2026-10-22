# EMA Hourly Continuation — ARPA/USDT P12_50

**Symbol:** ARPA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 781 |
| net_profit_factor | 0.7388 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 1.0137 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -3.2107 |
| sortino_ratio | -1.2820 |
| max_drawdown | 0.7797 |
| cagr | -0.4432 |
| net_avg_win | 57.0025 |
| net_avg_loss | -74.2441 |
| avg_hold_time_bars | 9.3880 |
| exposure | 0.3318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
