# EMA Hourly Continuation — UNI/USDT P20_26

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 134 |
| net_profit_factor | 0.7364 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0237 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -1.0774 |
| sortino_ratio | -0.1795 |
| max_drawdown | 0.2299 |
| cagr | -0.0788 |
| net_avg_win | 76.5330 |
| net_avg_loss | -107.0775 |
| avg_hold_time_bars | 4.8209 |
| exposure | 0.0294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
