# EMA Hourly Continuation — ARPA/USDT P8_89

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.5527 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.8542 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -6.1759 |
| sortino_ratio | -2.5587 |
| max_drawdown | 0.9581 |
| cagr | -0.7109 |
| net_avg_win | 30.7682 |
| net_avg_loss | -43.3630 |
| avg_hold_time_bars | 14.8027 |
| exposure | 0.5874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
