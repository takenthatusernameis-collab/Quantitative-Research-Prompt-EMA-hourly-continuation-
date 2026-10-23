# EMA Hourly Continuation — CELO/USDT P8_34

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1342 |
| net_profit_factor | 0.4918 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8791 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -8.0981 |
| sortino_ratio | -4.1657 |
| max_drawdown | 0.9940 |
| cagr | -0.8680 |
| net_avg_win | 16.0300 |
| net_avg_loss | -26.3579 |
| avg_hold_time_bars | 5.8316 |
| exposure | 0.3541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
