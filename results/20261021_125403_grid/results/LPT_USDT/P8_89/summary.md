# EMA Hourly Continuation — LPT/USDT P8_89

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.7776 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9519 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.1989 |
| sortino_ratio | -0.7279 |
| max_drawdown | 0.6182 |
| cagr | -0.2860 |
| net_avg_win | 77.0658 |
| net_avg_loss | -91.0237 |
| avg_hold_time_bars | 25.6562 |
| exposure | 0.6309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
