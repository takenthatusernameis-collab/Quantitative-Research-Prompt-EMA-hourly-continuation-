# EMA Hourly Continuation — AXL/USDT P8_89

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6690 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8031 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -3.3717 |
| sortino_ratio | -1.1750 |
| max_drawdown | 0.7579 |
| cagr | -0.4197 |
| net_avg_win | 56.1070 |
| net_avg_loss | -66.1547 |
| avg_hold_time_bars | 21.6230 |
| exposure | 0.5969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
