# EMA Hourly Continuation — JST/USDT P20_89

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6764 |
| net_win_rate | 0.5332 |
| gross_profit_factor | 1.1389 |
| gross_win_rate | 0.5332 |
| sharpe_ratio | -2.4030 |
| sortino_ratio | -0.7387 |
| max_drawdown | 0.5929 |
| cagr | -0.2920 |
| net_avg_win | 48.8220 |
| net_avg_loss | -82.4389 |
| avg_hold_time_bars | 17.4625 |
| exposure | 0.3690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
