# EMA Hourly Continuation — AVA/USDT P8_89

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 778 |
| net_profit_factor | 0.5677 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8926 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -4.4300 |
| sortino_ratio | -1.7222 |
| max_drawdown | 0.8880 |
| cagr | -0.5721 |
| net_avg_win | 31.1947 |
| net_avg_loss | -50.0909 |
| avg_hold_time_bars | 16.7095 |
| exposure | 0.5909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
