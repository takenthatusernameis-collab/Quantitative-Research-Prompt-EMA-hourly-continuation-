# EMA Hourly Continuation — ETC/USDT P8_89

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.5105 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8619 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -5.4787 |
| sortino_ratio | -2.0162 |
| max_drawdown | 0.9183 |
| cagr | -0.6261 |
| net_avg_win | 30.3134 |
| net_avg_loss | -50.2778 |
| avg_hold_time_bars | 20.8384 |
| exposure | 0.6507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
