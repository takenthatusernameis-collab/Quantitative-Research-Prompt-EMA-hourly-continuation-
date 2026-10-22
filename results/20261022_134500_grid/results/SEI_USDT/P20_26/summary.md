# EMA Hourly Continuation — SEI/USDT P20_26

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.3105 |
| net_win_rate | 0.3730 |
| gross_profit_factor | 0.7550 |
| gross_win_rate | 0.4112 |
| sharpe_ratio | -13.5562 |
| sortino_ratio | -6.7426 |
| max_drawdown | 0.9999 |
| cagr | -0.9706 |
| net_avg_win | 10.2554 |
| net_avg_loss | -19.6487 |
| avg_hold_time_bars | 1.8539 |
| exposure | 0.0992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
