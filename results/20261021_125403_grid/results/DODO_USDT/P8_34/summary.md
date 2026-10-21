# EMA Hourly Continuation — DODO/USDT P8_34

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 799 |
| net_profit_factor | 0.6793 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8886 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -3.5198 |
| sortino_ratio | -1.4150 |
| max_drawdown | 0.8074 |
| cagr | -0.4773 |
| net_avg_win | 45.4812 |
| net_avg_loss | -59.2182 |
| avg_hold_time_bars | 9.2240 |
| exposure | 0.3335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
