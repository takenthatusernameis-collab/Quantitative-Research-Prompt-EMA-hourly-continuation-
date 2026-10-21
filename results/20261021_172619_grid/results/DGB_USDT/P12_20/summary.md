# EMA Hourly Continuation — DGB/USDT P12_20

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.8273 |
| net_win_rate | 0.5393 |
| gross_profit_factor | 1.1898 |
| gross_win_rate | 0.5393 |
| sharpe_ratio | -1.0574 |
| sortino_ratio | -0.2558 |
| max_drawdown | 0.3618 |
| cagr | -0.1115 |
| net_avg_win | 81.4627 |
| net_avg_loss | -115.2611 |
| avg_hold_time_bars | 5.5357 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
