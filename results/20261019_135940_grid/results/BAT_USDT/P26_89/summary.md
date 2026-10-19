# EMA Hourly Continuation — BAT/USDT P26_89

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.5801 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9918 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -4.3132 |
| sortino_ratio | -1.6044 |
| max_drawdown | 0.8590 |
| cagr | -0.5375 |
| net_avg_win | 35.6182 |
| net_avg_loss | -55.5398 |
| avg_hold_time_bars | 10.2475 |
| exposure | 0.3256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
