# EMA Hourly Continuation — XEC/USDT P12_50

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1144 |
| net_profit_factor | 0.4902 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.9305 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -8.3463 |
| sortino_ratio | -3.9448 |
| max_drawdown | 0.9934 |
| cagr | -0.8609 |
| net_avg_win | 18.9449 |
| net_avg_loss | -30.4363 |
| avg_hold_time_bars | 7.1932 |
| exposure | 0.3724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
