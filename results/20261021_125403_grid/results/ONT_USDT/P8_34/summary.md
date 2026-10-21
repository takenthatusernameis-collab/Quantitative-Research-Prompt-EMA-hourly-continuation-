# EMA Hourly Continuation — ONT/USDT P8_34

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 785 |
| net_profit_factor | 0.6926 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -3.5623 |
| sortino_ratio | -1.4227 |
| max_drawdown | 0.8109 |
| cagr | -0.4783 |
| net_avg_win | 48.4484 |
| net_avg_loss | -63.9786 |
| avg_hold_time_bars | 7.9796 |
| exposure | 0.2835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
