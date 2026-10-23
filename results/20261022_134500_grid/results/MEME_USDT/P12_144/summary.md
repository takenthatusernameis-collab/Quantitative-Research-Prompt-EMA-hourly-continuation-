# EMA Hourly Continuation — MEME/USDT P12_144

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6835 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9256 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.6258 |
| sortino_ratio | -0.7797 |
| max_drawdown | 0.6230 |
| cagr | -0.3119 |
| net_avg_win | 61.1481 |
| net_avg_loss | -82.5547 |
| avg_hold_time_bars | 34.1696 |
| exposure | 0.6958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
