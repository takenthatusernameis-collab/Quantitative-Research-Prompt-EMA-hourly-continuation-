# EMA Hourly Continuation — ENJ/USDT P20_144

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7154 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 1.0365 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -2.3596 |
| sortino_ratio | -0.7228 |
| max_drawdown | 0.6142 |
| cagr | -0.2907 |
| net_avg_win | 62.8903 |
| net_avg_loss | -84.6109 |
| avg_hold_time_bars | 26.6285 |
| exposure | 0.5701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
