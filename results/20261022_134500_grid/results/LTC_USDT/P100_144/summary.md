# EMA Hourly Continuation — LTC/USDT P100_144

**Symbol:** LTC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.2307 |
| net_win_rate | 0.3800 |
| gross_profit_factor | 0.6932 |
| gross_win_rate | 0.4218 |
| sharpe_ratio | -8.7150 |
| sortino_ratio | -2.9442 |
| max_drawdown | 0.9783 |
| cagr | -0.7821 |
| net_avg_win | 14.0376 |
| net_avg_loss | -37.2905 |
| avg_hold_time_bars | 3.4109 |
| exposure | 0.0853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
