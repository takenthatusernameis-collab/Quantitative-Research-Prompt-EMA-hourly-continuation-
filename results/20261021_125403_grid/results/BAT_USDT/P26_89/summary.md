# EMA Hourly Continuation — BAT/USDT P26_89

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.7563 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0251 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -2.0534 |
| sortino_ratio | -0.6806 |
| max_drawdown | 0.5773 |
| cagr | -0.2681 |
| net_avg_win | 62.6883 |
| net_avg_loss | -84.1373 |
| avg_hold_time_bars | 12.8839 |
| exposure | 0.3127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
