# EMA Hourly Continuation — 1INCH/USDT P21_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6706 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.8685 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -2.7696 |
| sortino_ratio | -0.8264 |
| max_drawdown | 0.6316 |
| cagr | -0.3164 |
| net_avg_win | 61.7114 |
| net_avg_loss | -79.1517 |
| avg_hold_time_bars | 23.2005 |
| exposure | 0.4630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
