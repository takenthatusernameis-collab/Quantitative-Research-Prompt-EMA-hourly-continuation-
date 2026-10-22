# EMA Hourly Continuation — COTI/USDT P12_34

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.7913 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0186 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -1.7822 |
| sortino_ratio | -0.6267 |
| max_drawdown | 0.5509 |
| cagr | -0.2507 |
| net_avg_win | 64.3034 |
| net_avg_loss | -83.4606 |
| avg_hold_time_bars | 6.1217 |
| exposure | 0.1670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
