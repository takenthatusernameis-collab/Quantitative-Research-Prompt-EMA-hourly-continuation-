# EMA Hourly Continuation — APT/USDT P26_200

**Symbol:** APT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 1.0097 |
| net_win_rate | 0.5447 |
| gross_profit_factor | 1.1785 |
| gross_win_rate | 0.5447 |
| sharpe_ratio | 0.0967 |
| sortino_ratio | 0.0219 |
| max_drawdown | 0.1850 |
| cagr | 0.0047 |
| net_avg_win | 91.2701 |
| net_avg_loss | -108.1454 |
| avg_hold_time_bars | 54.8333 |
| exposure | 0.6131 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
