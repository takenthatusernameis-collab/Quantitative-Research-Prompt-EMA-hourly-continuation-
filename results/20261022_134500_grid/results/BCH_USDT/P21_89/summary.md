# EMA Hourly Continuation — BCH/USDT P21_89

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.4720 |
| net_win_rate | 0.4349 |
| gross_profit_factor | 0.8098 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -6.6172 |
| sortino_ratio | -2.5060 |
| max_drawdown | 0.9539 |
| cagr | -0.7055 |
| net_avg_win | 27.1455 |
| net_avg_loss | -44.2633 |
| avg_hold_time_bars | 11.1108 |
| exposure | 0.3646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
