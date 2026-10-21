# EMA Hourly Continuation — BTT/USDT P20_144

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.5971 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8830 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -3.4170 |
| sortino_ratio | -0.8933 |
| max_drawdown | 0.6490 |
| cagr | -0.3409 |
| net_avg_win | 62.4661 |
| net_avg_loss | -88.0328 |
| avg_hold_time_bars | 38.2285 |
| exposure | 0.5856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
