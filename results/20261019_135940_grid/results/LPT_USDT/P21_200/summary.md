# EMA Hourly Continuation — LPT/USDT P21_200

**Symbol:** LPT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6321 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -2.8753 |
| sortino_ratio | -0.8336 |
| max_drawdown | 0.6737 |
| cagr | -0.3240 |
| net_avg_win | 54.3191 |
| net_avg_loss | -74.9550 |
| avg_hold_time_bars | 30.6165 |
| exposure | 0.5915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
