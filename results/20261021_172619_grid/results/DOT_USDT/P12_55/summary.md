# EMA Hourly Continuation — DOT/USDT P12_55

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.7979 |
| net_win_rate | 0.5131 |
| gross_profit_factor | 1.0405 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -1.5529 |
| sortino_ratio | -0.5161 |
| max_drawdown | 0.4941 |
| cagr | -0.2115 |
| net_avg_win | 64.7539 |
| net_avg_loss | -85.5273 |
| avg_hold_time_bars | 16.5225 |
| exposure | 0.4010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
