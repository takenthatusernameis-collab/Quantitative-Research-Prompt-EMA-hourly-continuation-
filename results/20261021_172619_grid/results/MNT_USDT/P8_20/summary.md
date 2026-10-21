# EMA Hourly Continuation — MNT/USDT P8_20

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.5696 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -4.4051 |
| sortino_ratio | -1.5890 |
| max_drawdown | 0.8411 |
| cagr | -0.5177 |
| net_avg_win | 37.0499 |
| net_avg_loss | -58.9517 |
| avg_hold_time_bars | 6.2456 |
| exposure | 0.1791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
