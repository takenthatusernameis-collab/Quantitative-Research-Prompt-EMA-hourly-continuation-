# EMA Hourly Continuation — IO/USDT P26_89

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.6120 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8991 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -4.5060 |
| sortino_ratio | -1.7564 |
| max_drawdown | 0.8717 |
| cagr | -0.5745 |
| net_avg_win | 39.9758 |
| net_avg_loss | -57.5719 |
| avg_hold_time_bars | 7.8685 |
| exposure | 0.2781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
