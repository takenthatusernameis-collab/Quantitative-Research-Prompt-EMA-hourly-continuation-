# EMA Hourly Continuation — BTT/USDT P100_144

**Symbol:** BTT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.2488 |
| net_win_rate | 0.3125 |
| gross_profit_factor | 0.7136 |
| gross_win_rate | 0.4012 |
| sharpe_ratio | -10.2641 |
| sortino_ratio | -3.4280 |
| max_drawdown | 0.9903 |
| cagr | -0.8412 |
| net_avg_win | 21.1588 |
| net_avg_loss | -38.6547 |
| avg_hold_time_bars | 5.2802 |
| exposure | 0.1190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
