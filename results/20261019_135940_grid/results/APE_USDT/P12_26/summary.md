# EMA Hourly Continuation — APE/USDT P12_26

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1388 |
| net_profit_factor | 0.3534 |
| net_win_rate | 0.4251 |
| gross_profit_factor | 0.7861 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -10.9135 |
| sortino_ratio | -5.7500 |
| max_drawdown | 0.9993 |
| cagr | -0.9435 |
| net_avg_win | 9.2560 |
| net_avg_loss | -19.3656 |
| avg_hold_time_bars | 2.7320 |
| exposure | 0.1724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
