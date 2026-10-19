# EMA Hourly Continuation — FET/USDT P34_89

**Symbol:** FET/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.6403 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -3.4985 |
| sortino_ratio | -1.2293 |
| max_drawdown | 0.7791 |
| cagr | -0.4399 |
| net_avg_win | 45.4930 |
| net_avg_loss | -67.0301 |
| avg_hold_time_bars | 8.9887 |
| exposure | 0.2525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
