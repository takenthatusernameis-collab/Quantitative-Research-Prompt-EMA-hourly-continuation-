# EMA Hourly Continuation — GTC/USDT P12_34

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1172 |
| net_profit_factor | 0.4618 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.8622 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -8.4280 |
| sortino_ratio | -4.0637 |
| max_drawdown | 0.9934 |
| cagr | -0.8628 |
| net_avg_win | 16.6803 |
| net_avg_loss | -27.9205 |
| avg_hold_time_bars | 4.6323 |
| exposure | 0.2468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
