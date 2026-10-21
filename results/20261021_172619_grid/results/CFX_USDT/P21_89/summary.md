# EMA Hourly Continuation — CFX/USDT P21_89

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7594 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9577 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -1.8900 |
| sortino_ratio | -0.5772 |
| max_drawdown | 0.5177 |
| cagr | -0.2333 |
| net_avg_win | 68.5892 |
| net_avg_loss | -86.8336 |
| avg_hold_time_bars | 18.1094 |
| exposure | 0.3762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
