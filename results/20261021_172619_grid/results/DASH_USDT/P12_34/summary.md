# EMA Hourly Continuation — DASH/USDT P12_34

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.7673 |
| net_win_rate | 0.5158 |
| gross_profit_factor | 1.0651 |
| gross_win_rate | 0.5158 |
| sharpe_ratio | -1.8314 |
| sortino_ratio | -0.6110 |
| max_drawdown | 0.5134 |
| cagr | -0.2444 |
| net_avg_win | 60.1357 |
| net_avg_loss | -83.5000 |
| avg_hold_time_bars | 7.3911 |
| exposure | 0.1804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
