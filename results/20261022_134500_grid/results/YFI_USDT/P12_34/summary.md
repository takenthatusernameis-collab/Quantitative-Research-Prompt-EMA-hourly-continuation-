# EMA Hourly Continuation — YFI/USDT P12_34

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1394 |
| net_profit_factor | 0.3240 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 0.8473 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -12.0344 |
| sortino_ratio | -6.3618 |
| max_drawdown | 0.9997 |
| cagr | -0.9609 |
| net_avg_win | 8.3057 |
| net_avg_loss | -18.1023 |
| avg_hold_time_bars | 4.1499 |
| exposure | 0.2618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
