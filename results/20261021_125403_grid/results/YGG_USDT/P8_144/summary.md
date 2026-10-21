# EMA Hourly Continuation — YGG/USDT P8_144

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.8937 |
| net_win_rate | 0.5116 |
| gross_profit_factor | 1.0540 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -0.7757 |
| sortino_ratio | -0.2304 |
| max_drawdown | 0.3648 |
| cagr | -0.1042 |
| net_avg_win | 92.6153 |
| net_avg_loss | -108.5681 |
| avg_hold_time_bars | 36.7698 |
| exposure | 0.7155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
