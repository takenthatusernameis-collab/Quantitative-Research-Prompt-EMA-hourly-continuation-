# EMA Hourly Continuation — IO/USDT P34_89

**Symbol:** IO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.5815 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.8678 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -4.5657 |
| sortino_ratio | -1.7369 |
| max_drawdown | 0.8623 |
| cagr | -0.5637 |
| net_avg_win | 37.3913 |
| net_avg_loss | -56.1999 |
| avg_hold_time_bars | 6.2617 |
| exposure | 0.2073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
