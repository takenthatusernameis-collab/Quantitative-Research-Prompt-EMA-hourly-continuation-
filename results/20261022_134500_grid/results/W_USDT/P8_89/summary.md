# EMA Hourly Continuation — W/USDT P8_89

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.7744 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0554 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -2.0916 |
| sortino_ratio | -0.7518 |
| max_drawdown | 0.6443 |
| cagr | -0.3044 |
| net_avg_win | 61.0905 |
| net_avg_loss | -84.1483 |
| avg_hold_time_bars | 22.3103 |
| exposure | 0.6602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
