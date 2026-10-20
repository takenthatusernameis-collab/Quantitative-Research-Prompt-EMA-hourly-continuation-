# EMA Hourly Continuation — CTC/USDT P34_89

**Symbol:** CTC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.5107 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.9175 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -5.8849 |
| sortino_ratio | -2.1677 |
| max_drawdown | 0.9362 |
| cagr | -0.6552 |
| net_avg_win | 31.5446 |
| net_avg_loss | -50.4668 |
| avg_hold_time_bars | 7.6584 |
| exposure | 0.2385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
