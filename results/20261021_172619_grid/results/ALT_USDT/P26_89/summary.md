# EMA Hourly Continuation — ALT/USDT P26_89

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.8301 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0386 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.2287 |
| sortino_ratio | -0.3849 |
| max_drawdown | 0.3852 |
| cagr | -0.1640 |
| net_avg_win | 72.5616 |
| net_avg_loss | -91.9331 |
| avg_hold_time_bars | 14.8109 |
| exposure | 0.3205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
