# EMA Hourly Continuation — KSM/USDT P21_89

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.5260 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8776 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -5.3724 |
| sortino_ratio | -1.9574 |
| max_drawdown | 0.9145 |
| cagr | -0.6190 |
| net_avg_win | 32.9390 |
| net_avg_loss | -51.5449 |
| avg_hold_time_bars | 12.7147 |
| exposure | 0.3930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
