# EMA Hourly Continuation — WAVES/USDT P34_89

**Symbol:** WAVES/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 816 |
| net_profit_factor | 0.4227 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.7669 |
| gross_win_rate | 0.4314 |
| sharpe_ratio | -7.8799 |
| sortino_ratio | -3.1669 |
| max_drawdown | 0.9815 |
| cagr | -0.7957 |
| net_avg_win | 21.0764 |
| net_avg_loss | -35.7932 |
| avg_hold_time_bars | 6.9914 |
| exposure | 0.2593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
