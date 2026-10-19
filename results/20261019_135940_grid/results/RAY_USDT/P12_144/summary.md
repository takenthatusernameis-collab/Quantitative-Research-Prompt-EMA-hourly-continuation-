# EMA Hourly Continuation — RAY/USDT P12_144

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6994 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9598 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.5934 |
| sortino_ratio | -0.8420 |
| max_drawdown | 0.6542 |
| cagr | -0.3267 |
| net_avg_win | 57.9138 |
| net_avg_loss | -75.6269 |
| avg_hold_time_bars | 26.2132 |
| exposure | 0.6315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
