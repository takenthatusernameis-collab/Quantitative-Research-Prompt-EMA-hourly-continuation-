# EMA Hourly Continuation — ACE/USDT P12_50

**Symbol:** ACE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 818 |
| net_profit_factor | 0.6420 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9958 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -3.8177 |
| sortino_ratio | -1.5459 |
| max_drawdown | 0.8408 |
| cagr | -0.5127 |
| net_avg_win | 37.4231 |
| net_avg_loss | -56.0566 |
| avg_hold_time_bars | 10.0746 |
| exposure | 0.3729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
