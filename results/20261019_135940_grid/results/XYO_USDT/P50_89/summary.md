# EMA Hourly Continuation — XYO/USDT P50_89

**Symbol:** XYO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 783 |
| net_profit_factor | 0.3907 |
| net_win_rate | 0.3985 |
| gross_profit_factor | 0.8140 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -8.9066 |
| sortino_ratio | -3.5362 |
| max_drawdown | 0.9892 |
| cagr | -0.8325 |
| net_avg_win | 20.3280 |
| net_avg_loss | -34.4631 |
| avg_hold_time_bars | 4.9885 |
| exposure | 0.1768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
