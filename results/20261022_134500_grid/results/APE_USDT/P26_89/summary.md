# EMA Hourly Continuation — APE/USDT P26_89

**Symbol:** APE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.5640 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.8985 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -4.5486 |
| sortino_ratio | -1.7384 |
| max_drawdown | 0.8821 |
| cagr | -0.5665 |
| net_avg_win | 32.2481 |
| net_avg_loss | -51.8700 |
| avg_hold_time_bars | 8.6365 |
| exposure | 0.2905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
