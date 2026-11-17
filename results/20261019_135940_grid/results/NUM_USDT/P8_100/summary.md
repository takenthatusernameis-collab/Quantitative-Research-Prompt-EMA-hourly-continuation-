# EMA Hourly Continuation — NUM/USDT P8_100

**Symbol:** NUM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.5561 |
| net_win_rate | 0.3951 |
| gross_profit_factor | 0.7931 |
| gross_win_rate | 0.4019 |
| sharpe_ratio | -6.1595 |
| sortino_ratio | -2.3436 |
| max_drawdown | 0.9437 |
| cagr | -0.6727 |
| net_avg_win | 40.3083 |
| net_avg_loss | -47.3489 |
| avg_hold_time_bars | 18.3640 |
| exposure | 0.6169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
