# EMA Hourly Continuation — ETHFI/USDT P12_21

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7407 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9409 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -1.6166 |
| sortino_ratio | -0.3901 |
| max_drawdown | 0.3831 |
| cagr | -0.1644 |
| net_avg_win | 75.1526 |
| net_avg_loss | -95.2483 |
| avg_hold_time_bars | 5.7088 |
| exposure | 0.0740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
