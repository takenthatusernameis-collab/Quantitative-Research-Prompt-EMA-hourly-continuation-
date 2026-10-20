# EMA Hourly Continuation — SYN/USDT P34_55

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 880 |
| net_profit_factor | 0.4618 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.8469 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -7.1466 |
| sortino_ratio | -2.9768 |
| max_drawdown | 0.9757 |
| cagr | -0.7721 |
| net_avg_win | 21.5210 |
| net_avg_loss | -36.9203 |
| avg_hold_time_bars | 3.7659 |
| exposure | 0.1506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
