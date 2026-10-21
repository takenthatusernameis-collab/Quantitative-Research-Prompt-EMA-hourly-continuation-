# EMA Hourly Continuation — DGB/USDT P12_89

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.8562 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0681 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.1882 |
| sortino_ratio | -0.4037 |
| max_drawdown | 0.4075 |
| cagr | -0.1720 |
| net_avg_win | 78.0367 |
| net_avg_loss | -96.8631 |
| avg_hold_time_bars | 19.3005 |
| exposure | 0.4904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
