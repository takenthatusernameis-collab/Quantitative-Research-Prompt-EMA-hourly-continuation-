# EMA Hourly Continuation — W/USDT P55_89

**Symbol:** W/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.4787 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8166 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -5.2798 |
| sortino_ratio | -1.8968 |
| max_drawdown | 0.9063 |
| cagr | -0.6034 |
| net_avg_win | 27.6135 |
| net_avg_loss | -48.8803 |
| avg_hold_time_bars | 4.1896 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
