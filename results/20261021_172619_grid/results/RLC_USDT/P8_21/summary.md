# EMA Hourly Continuation — RLC/USDT P8_21

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.6851 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -3.6052 |
| sortino_ratio | -1.4107 |
| max_drawdown | 0.8272 |
| cagr | -0.4745 |
| net_avg_win | 48.0256 |
| net_avg_loss | -66.7884 |
| avg_hold_time_bars | 5.3575 |
| exposure | 0.1812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
