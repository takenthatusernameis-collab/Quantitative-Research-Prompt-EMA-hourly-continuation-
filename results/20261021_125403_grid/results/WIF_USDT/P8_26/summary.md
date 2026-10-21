# EMA Hourly Continuation — WIF/USDT P8_26

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.9127 |
| net_win_rate | 0.5298 |
| gross_profit_factor | 1.1203 |
| gross_win_rate | 0.5298 |
| sharpe_ratio | -0.6905 |
| sortino_ratio | -0.2380 |
| max_drawdown | 0.4040 |
| cagr | -0.1091 |
| net_avg_win | 87.1616 |
| net_avg_loss | -107.6168 |
| avg_hold_time_bars | 6.9842 |
| exposure | 0.1810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
