# EMA Hourly Continuation — INJ/USDT P50_100

**Symbol:** INJ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.5855 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.9243 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -4.3158 |
| sortino_ratio | -1.4805 |
| max_drawdown | 0.8426 |
| cagr | -0.5177 |
| net_avg_win | 41.6280 |
| net_avg_loss | -63.5163 |
| avg_hold_time_bars | 4.9570 |
| exposure | 0.1361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
