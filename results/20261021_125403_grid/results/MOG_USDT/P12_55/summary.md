# EMA Hourly Continuation — MOG/USDT P12_55

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.8313 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9769 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -1.6903 |
| sortino_ratio | -0.6021 |
| max_drawdown | 0.5556 |
| cagr | -0.2440 |
| net_avg_win | 83.7302 |
| net_avg_loss | -96.8970 |
| avg_hold_time_bars | 12.2232 |
| exposure | 0.3457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
