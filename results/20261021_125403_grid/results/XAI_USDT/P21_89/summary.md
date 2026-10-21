# EMA Hourly Continuation — XAI/USDT P21_89

**Symbol:** XAI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7765 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9537 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -2.2582 |
| sortino_ratio | -0.7478 |
| max_drawdown | 0.6552 |
| cagr | -0.2917 |
| net_avg_win | 78.0410 |
| net_avg_loss | -91.9443 |
| avg_hold_time_bars | 15.9148 |
| exposure | 0.3906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
