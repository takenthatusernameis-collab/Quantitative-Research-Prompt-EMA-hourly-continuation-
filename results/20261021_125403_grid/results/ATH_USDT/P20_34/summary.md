# EMA Hourly Continuation — ATH/USDT P20_34

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8681 |
| net_win_rate | 0.5370 |
| gross_profit_factor | 1.1556 |
| gross_win_rate | 0.5370 |
| sharpe_ratio | -0.7302 |
| sortino_ratio | -0.1793 |
| max_drawdown | 0.2098 |
| cagr | -0.0806 |
| net_avg_win | 81.5280 |
| net_avg_loss | -108.9390 |
| avg_hold_time_bars | 4.8704 |
| exposure | 0.0637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
