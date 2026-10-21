# EMA Hourly Continuation — REQ/USDT P12_21

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.4975 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.8835 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -5.6324 |
| sortino_ratio | -1.7568 |
| max_drawdown | 0.8747 |
| cagr | -0.5607 |
| net_avg_win | 42.3766 |
| net_avg_loss | -66.3270 |
| avg_hold_time_bars | 4.7768 |
| exposure | 0.1012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
