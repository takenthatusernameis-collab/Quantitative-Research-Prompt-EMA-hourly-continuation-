# EMA Hourly Continuation — XYO/USDT P34_89

**Symbol:** XYO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.4091 |
| net_win_rate | 0.3920 |
| gross_profit_factor | 0.8096 |
| gross_win_rate | 0.4160 |
| sharpe_ratio | -8.4280 |
| sortino_ratio | -3.2605 |
| max_drawdown | 0.9841 |
| cagr | -0.8045 |
| net_avg_win | 23.1606 |
| net_avg_loss | -36.5049 |
| avg_hold_time_bars | 7.8107 |
| exposure | 0.2651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
