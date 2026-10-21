# EMA Hourly Continuation — ENJ/USDT P26_144

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8367 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0252 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -1.0988 |
| sortino_ratio | -0.3037 |
| max_drawdown | 0.3919 |
| cagr | -0.1322 |
| net_avg_win | 81.5485 |
| net_avg_loss | -99.5677 |
| avg_hold_time_bars | 29.2086 |
| exposure | 0.4943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
