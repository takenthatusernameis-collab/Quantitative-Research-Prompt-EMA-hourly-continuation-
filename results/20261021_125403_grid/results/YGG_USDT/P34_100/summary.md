# EMA Hourly Continuation — YGG/USDT P34_100

**Symbol:** YGG/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7811 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9839 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.7136 |
| sortino_ratio | -0.5356 |
| max_drawdown | 0.4959 |
| cagr | -0.2188 |
| net_avg_win | 69.4821 |
| net_avg_loss | -87.8506 |
| avg_hold_time_bars | 12.6138 |
| exposure | 0.2734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
