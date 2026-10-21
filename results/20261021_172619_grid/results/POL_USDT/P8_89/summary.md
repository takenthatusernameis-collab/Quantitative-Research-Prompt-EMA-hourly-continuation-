# EMA Hourly Continuation — POL/USDT P8_89

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7877 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3670 |
| sortino_ratio | -0.3831 |
| max_drawdown | 0.4176 |
| cagr | -0.1628 |
| net_avg_win | 69.5410 |
| net_avg_loss | -88.2874 |
| avg_hold_time_bars | 39.6458 |
| exposure | 0.6920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
