# EMA Hourly Continuation — BTT/USDT P21_89

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.3561 |
| net_win_rate | 0.3642 |
| gross_profit_factor | 0.7211 |
| gross_win_rate | 0.4030 |
| sharpe_ratio | -9.7489 |
| sortino_ratio | -3.6324 |
| max_drawdown | 0.9914 |
| cagr | -0.8498 |
| net_avg_win | 22.4760 |
| net_avg_loss | -36.1470 |
| avg_hold_time_bars | 14.0119 |
| exposure | 0.4267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
