# EMA Hourly Continuation — YFI/USDT P8_55

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1179 |
| net_profit_factor | 0.4063 |
| net_win_rate | 0.4309 |
| gross_profit_factor | 0.8238 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -8.8645 |
| sortino_ratio | -4.2829 |
| max_drawdown | 0.9953 |
| cagr | -0.8793 |
| net_avg_win | 13.4048 |
| net_avg_loss | -24.9797 |
| avg_hold_time_bars | 9.2103 |
| exposure | 0.4914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
