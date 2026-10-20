# EMA Hourly Continuation — AXL/USDT P55_89

**Symbol:** AXL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.4934 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.8431 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -6.2438 |
| sortino_ratio | -2.4026 |
| max_drawdown | 0.9488 |
| cagr | -0.6911 |
| net_avg_win | 27.9896 |
| net_avg_loss | -44.2556 |
| avg_hold_time_bars | 3.9761 |
| exposure | 0.1355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
